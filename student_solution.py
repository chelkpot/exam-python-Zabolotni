# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)

    s=(input().split(","))
    print(len(s[0])>len(s[1]))
    print(len(s[0])==len(s[1]))
    print(s[0] in s[1])

    #s=(input().split(","))
    #print((len(s[0])>len(s[1]), len(s[0])==len(s[1]), s[0] in s[1]))

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())

    s=input()
    print(s.strip())
    print(len(s))
    print(s.count("a"))
    print(s.replace("a", "@"))
    print(s.istitle())

    #s=input()
    #print((s.strip(), len(s), s.count("a"), s.replace("a", "@"), s.istitle()))

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)

    s=input()
    print(s[1:-1])
    print(s[1::2])
    print(s[::-1].lower())

    #s=input()
    #print((s[1:-1], s[1::2], s[::-1].lower()))

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))

    nums=list(map(int, input().split(" ")))
    nums.sort()
    print(nums)
    print(sum(nums))
    print(min(nums), max(nums))

    #nums=list(map(int, input().split(" ")))
    #s.sort()
    #print((s, sum(s), (s[0], s[-1])))


# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False

    s=input()
    print(s[::-1].lower()==s.lower() and s.count(" ")==0)

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)

    n=hex(int(input()))
    print(str(n).strip("0x"))
    print(len(str(n).strip("0x")))
    print(n in str(n).strip("0x"))

    #s=hex(int(input()))
    #print(str(s).strip("0x"), len(str(s).strip("0x")), s in str(s).strip("0x"))

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    
    a=int(input())-1
    print(months[a])
