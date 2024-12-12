# Fast Fourier transform
# Load the (complex) signal from .csv file, assert input data,
# compute (Radix-2) Fast-fourier transform, and store the result into output file

import argparse
import csv
import cmath

# Radix-2 FFT algorithm
# refer to https://stackoverflow.com/questions/28009590/understanding-the-radix-2-fft-recursive-algorithm
def fft2(data):
    assert(type(data) is list or tuple)
    assert(len(data) != 0)
    if len(data) == 1:
        return data
    # else
    assert(len(data) % 2 == 0)
    omega_n = [0] * len(data)
    for i in range(len(data)):
        omega_n[i] = cmath.exp(2 * cmath.pi * i * 1j / len(data))
    # extract odd indices components
    odds = data[0::2]
    # extract even indices components
    evens = data[1::2]

    result_odds = fft2(odds)
    result_evens = fft2(evens)
    result = [0] * len(data)
    for i in range(len(result_odds)):
        result[i] = result_odds[i] + result_evens[i] * omega_n[i]
        result[i+len(result_odds)] = result_odds[i] - result_evens[i] * omega_n[i]
        pass

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="fast_fourier_transform.py",
                                    description="Compute the fast (Radix-2) Fourier transform of the input, and store it into the output.")

    parser.add_argument('input', help="Input .csv file", type=str)
    # NOTE: could create output filename from input filename
    parser.add_argument('output', help="Output filename", type=str)

    # parse input arguments
    args = parser.parse_args()

    # for filename in parser.input:
    #     with open(filename, "r") as file:
    #         data.append(csv.reader(file, delimiter=','))

    filename = args.input
    input_file = open(filename, "r")
    reader = csv.reader(input_file, delimiter=',')
    output_file = open(args.output, "w")
    writer = csv.writer(output_file)

    for row in reader:
        for index in range(len(row)):
            row[index] = complex(row[index].replace(" ", "").replace("i", "j"))
        # print(row)
        data_fft = fft2(row)
        for i in range(len(data_fft)):
            data_fft[i] = round(data_fft[i].real, 7) + round(data_fft[i].imag, 7) * 1j
        writer.writerow(data_fft)

    print("Normal exit.")
