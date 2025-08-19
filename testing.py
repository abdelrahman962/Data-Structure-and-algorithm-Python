def bubble(arr,n):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



arr=[5,4,3,2,1]

print(bubble(arr,len(arr)))
name = "abd masri"
first, last = name.strip().title().split()  # Split the name after stripping and titling
print(f"hello: {first}",end="\n")

x=float(input("x: "))
y=float(input("y: "))
z=round(x/y)
print(f"{z:,}")

 