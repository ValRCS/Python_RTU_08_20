# let's test tqdm progress bar
# tqdm is useful for showing progress bar
# if you need to process a large amount of data and want to show the progress
# you can use tqdm
# try importing
try:
    from tqdm import tqdm
    print("tqdm is installed")
except ImportError:
    print("tqdm is not installed")
    print("Please install tqdm using pip with the following command:")
    print("pip install tqdm")

total = 0

# let's test tqdm progress bar
for n in tqdm(range(10_000_000)):
    total += n

print(f"Total is {total}")
