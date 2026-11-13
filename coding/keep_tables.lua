-- Reserve enough space for these short tables and their Markdown captions.
-- The data and captions remain in the report source.
local space = { ["1"] = 190, ["2"] = 105, ["3"] = 100,
                ["4"] = 105, ["5"] = 115, ["6"] = 110,
                ["7"] = 100, ["A1"] = 170 }

local function keep_caption(block)
  local label = pandoc.utils.stringify(block):match("^Table ([%dA]+)%.")
  if label and space[label] then
    return { pandoc.RawBlock('latex', '\\Needspace{' .. space[label] .. 'pt}'), block }
  end
end

local function keep_heading(block)
  if pandoc.utils.stringify(block):match('^Appendix A') then
    return { pandoc.RawBlock('latex', '\\Needspace{220pt}'), block }
  end
end

function Pandoc(doc)
  local filters = { Para = keep_caption, Header = keep_heading }
  if pandoc.utils.stringify(doc.meta['report-source'] or '') == 'REPORT_VER2.md' then
    space = { ["1"] = 90, ["2"] = 100, ["3"] = 95, ["4"] = 115, ["5"] = 100 }
    local legacy_heading = keep_heading
    keep_heading = function(block)
      if pandoc.utils.stringify(block) == 'References' then
        return { pandoc.RawBlock('latex', '\\Needspace{140pt}'), block }
      end
      return legacy_heading(block)
    end
    filters.Header = keep_heading
    filters.Blocks = function(blocks)
      local result = {}
      for i, block in ipairs(blocks) do
        local following = blocks[i + 1]
        if block.t == 'Para' and following and following.t == 'Para'
          and #following.content == 1 and following.content[1].t == 'Math'
          and following.content[1].mathtype == 'DisplayMath' then
          result[#result + 1] = pandoc.RawBlock('latex', '\\Needspace{85pt}')
        end
        result[#result + 1] = block
      end
      return result
    end
  end
  return doc:walk(filters)
end
