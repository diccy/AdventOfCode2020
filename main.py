
import  d1,  d2,  d3,  d4,  d5,  d6,  d7,  d8,  d9, d10
import d11, d12, d13, d14, d15, d16, d17, d18#, d19, d20
#import d21, d22, d23, d24

from time import time

def main():

    days = {
        'd1':  d1,
        'd2':  d2,
        'd3':  d3,
        'd4':  d4,
        'd5':  d5,
        'd6':  d6,
        'd7':  d7,
        'd8':  d8,
        'd9':  d9,
        'd10': d10,
        'd11': d11,
        'd12': d12,
        'd13': d13,
        'd14': d14,
        'd15': d15,
        'd16': d16,
        'd17': d17,
        'd18': d18,
        #'d19': d19,
        #'d20': d20,
        #'d21': d21,
        #'d22': d22,
        #'d23': d23,
        #'d24': d24,
    }

    summary = []
    print('')
    for day_name, v in days.items():
        print(f'{day_name}...')
        start_t = time()
        v.Resolve(True)
        end_t = time()
        elapsed = end_t - start_t
        if elapsed < 1.0:
            sum = 0.0
            count = int(1.0 / max(elapsed, 0.001))
            for _ in range(count):
                start_t = time()
                v.Resolve(False)
                sum += time() - start_t
            elapsed = sum / count
        elapsed *= 1000.0
        print(f'{day_name}: {elapsed:.3f}ms\n')
        summary.append((day_name, elapsed))

    print('\nSommaire gaulois:')
    for day_name, t in summary:
        print(f'{day_name}: {t:.3f}ms')

main()
