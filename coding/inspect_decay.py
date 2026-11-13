"""Print the selected extrema and sensitivity checks from the report analysis."""
import json
from analyse_results import DECAY_STARTS, decay, load_all


def main():
    records = load_all()
    for key, start in DECAY_STARTS.items():
        result = decay(records[key], start)
        print(key)
        print(json.dumps({name: value for name, value in result.items()
                          if name != 'peak_indices'}, indent=2))
        print('Selected maxima: time (s), raw response (mV)')
        for index in result['peak_indices']:
            print(*records[key]['wave'][index])


if __name__ == '__main__':
    main()
