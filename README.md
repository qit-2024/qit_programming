# QIT-2024 Programming class
## Evaluation code sample -- Yurii Kravets
### Radix-2 Fast-Fourier-Transform (FFT) algorithm

Discrete Fourier Transform (DFT) is the base apparatus used in frequency analysis of discrete signals.

Cooley-Tukey's Fast Fourier Transform (FFT) algorithm, being the topic of this code sample, was proposed in 1965 by James W. Cooley and John W. Tukey.

The main advantage of algorithm is reduced computation cost of Fourier Transform ($O(N*log(N))$ instead of $O(N^2)$ achieved by Direct Fourier Transform).

The disadvantages of discussed algorithm are the following:
1. *Radix-2* number of samples in input signal -- reduced suitability for signals of length numbers that contain other primes than 2;
2. *Recursion* used in the algorithm may incur to increased memory and/or call stack usage.

### Code sample in this repository

The main code sample is stored in `fast_fourier_transform.py` file. Presented sample code has the following structure:

1. *Importing necessary modules*: the modules in use are:
   * `argparse`: argument parser used in cases where the code sample is invoked as a program (general use-case scenario);
   * `cmath`: complex mathematical functions (`exp()` function used for computing complex exponential values);
   * `csv` module used to load-from and store the data into `.csv` (*Comma-Separated-Values*) files;
2. Defining `fft2()` function as follows (notice the recursive calls):
   ```python
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
   ```
   3. Handling `"__main__"` context, if the file is called in main context (that is not being imported):
   ```python
   if __name__ == "__main__":
      parser = argparse.ArgumentParser(...)
   ```
   (will not further focus on the code).

### Usage

There are two basic scenarios for calling the `fft2()` function:
1. `import`ing the `fast_fourier_transform` module allows calling `fft2()` function directly:
```python
data = [1, -1, 1, -1]
data_fft = fft2(data)
print(data_fft)
```
2. Calling `fast_fourier_transform.py` as the `main` context, which expects two positional arguments, `input` and `output` filenames. For example:
```bash
$ python3 fast_fourier_transform.py sample.csv output.csv
```
(notice *sample.csv* file has been included into the repository index. Also note the `i` and `j` imaginary number indicators are used interchangeably).

The content of *sample.csv* is:
```csv
0+1i,0-1i,0+1i,0-1i
1,2,3,4
1,-1,1,-1
```

Notice the `fast_fourier_transform` module, when called in `"__main__"` context, computes and stores Fourier Transforms column-wise. Then the expected **output** file content would be:

```csv
0,0,4j,0
10,-2+2i,-2,2-2i
0,0,4,0
```

Although generally this is true, the floating-point calculations produce imprecisions shown in the output sample below:

```csv
0j,0j,4j,0j
(10+0j),(-2-2j),(-2+0j),(-1.9999999999999998+2j)
0j,0j,(4+0j),0j
```

In order to reduce the floating-point calculation imprecisions in the output files, the `round()` method is called in order to arbitrarily reduce the precision of the result up to 7 most-significant digits.
