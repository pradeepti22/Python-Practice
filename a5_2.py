largest = None
smallest = None
while True:
    nums = input('Enter Number: ')
    if nums == "done":
        break
    else:
        try:
            numi = int(nums)
            if largest is None:
                largest = numi
            if smallest is None:
                smallest = numi
            if numi > largest:
                largest = numi
            if numi < smallest:
                smallest = numi
        except:
            print('Invalid input')
            continue
print('Maximum is', largest)
print('Minimum is', smallest)
