-- Reserve enough space for these short tables and their Markdown captions.
-- The data and captions remain in the report source.
local space = { ["1"] = 190, ["2"] = 105, ["3"] = 100,
                ["4"] = 105, ["5"] = 115, ["6"] = 110,
                ["7"] = 100, ["A1"] = 170 }

function Para(block)
  local label = pandoc.utils.stringify(block):match("^Table ([%dA]+)%.")
  if label and space[label] then
    return { pandoc.RawBlock('latex', '\\Needspace{' .. space[label] .. 'pt}'), block }
  end
end

function Header(block)
  if pandoc.utils.stringify(block):match('^Appendix A') then
    return { pandoc.RawBlock('latex', '\\Needspace{220pt}'), block }
  end
end
