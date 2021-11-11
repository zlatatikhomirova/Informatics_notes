# (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z).

# def f(n):
#     if not n:
#         print(1)
#         return
#     n -= 1

#   for i in (0, 1):
#     foo(n)
    
    
arr = []
# добавить названия переменных
F = 1
expr = "x or y and z"
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if eval(expr) == F:
                arr.append([x, y, z, F])

print(arr)
                
                
