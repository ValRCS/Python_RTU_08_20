# general syntax for while loop

start = 0
end = 100
step = 25
i = start
while i < end: # we do not include end in this example for that we need i<=end
    print(f"i is now {i}")
    i += step
    
print("i is ",i)

# this works, but perhaps there is another syntax to do this using different loop?