# 📘 Session 1 — Step 4: NumPy Data Types

Data types define what kind of values an array contains and how NumPy stores those values in memory.

NumPy supports common Python data types such as integers, floats, booleans and strings, but it also provides its own data type system using short codes such as `i`, `u`, `f`, `S` and `U`.

---

## 🎯 هدف این مرحله

در این مرحله یاد می‌گیریم:

* Python Data Types چیست
* NumPy Data Types چیست
* `dtype` چه کاری انجام می‌دهد
* چگونه نوع داده‌ی یک Array را مشخص کنیم
* Size در Data Type چیست
* `ValueError` هنگام تبدیل نوع داده
* چگونه با `astype()` نوع داده‌ی یک Array موجود را تغییر دهیم
* تفاوت `dtype` و `astype()`

---

# 1️⃣ Data Types in Python

Python دارای Data Typeهای مختلفی است:

| Type      | Description    | Example    |
| --------- | -------------- | ---------- |
| `str`     | Text           | `"Hello"`  |
| `int`     | Integer number | `10`, `-5` |
| `float`   | Decimal number | `10.5`     |
| `bool`    | True or False  | `True`     |
| `complex` | Complex number | `1 + 2j`   |

NumPy نیز از این نوع داده‌ها پشتیبانی می‌کند، اما سیستم Data Type آن دقیق‌تر است.

---

# 2️⃣ NumPy Data Types

NumPy برای Data Typeها معمولاً از حروف کوتاه استفاده می‌کند:

| Code | Type              |
| ---- | ----------------- |
| `i`  | Integer           |
| `b`  | Boolean           |
| `u`  | Unsigned Integer  |
| `f`  | Float             |
| `c`  | Complex Float     |
| `m`  | Timedelta         |
| `M`  | Datetime          |
| `O`  | Object            |
| `S`  | String            |
| `U`  | Unicode String    |
| `V`  | Void / Raw Memory |

مثلاً:

```python
'i'     # integer
'f'     # float
'b'     # boolean
'S'     # string
```

---

# 3️⃣ Checking Data Type with dtype

هر NumPy Array دارای ویژگی `dtype` است.

با استفاده از آن می‌توانیم نوع داده‌ی عناصر Array را مشاهده کنیم:

```python
import numpy as np

a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array(["Hello", "World!"])

print(a_array.dtype)
print(b_array.dtype)
```

### Output:

```text
int64
<U6
```

در این مثال:

```python
a_array.dtype
```

نشان می‌دهد که Array شامل Integer است.

و:

```python
b_array.dtype
```

نشان می‌دهد که Array شامل Unicode String است.

> 📌 نوع دقیق خروجی مثل `int64` ممکن است با توجه به سیستم شما متفاوت باشد.

---

# 4️⃣ Defining Data Type with dtype

هنگام ساخت Array می‌توانیم Data Type را خودمان مشخص کنیم.

برای این کار از `dtype` استفاده می‌کنیم:

```python
c_array = np.array(
    [1, 2, 3, 4, 5],
    dtype='S'
)

print(c_array)
print(c_array.dtype)
```

### Output:

```text
[b'1' b'2' b'3' b'4' b'5']
|S1
```

در اینجا به NumPy گفتیم که داده‌ها را به صورت String ذخیره کند.

---

# 5️⃣ Data Type Size

برای بعضی Data Typeها می‌توانیم Size را نیز مشخص کنیم.

مثلاً:

```python
'i4'
```

یعنی Integer با اندازه‌ی 4 Byte.

مثال:

```python
array_4byte = np.array(
    [1, 2, 3, 4, 5],
    dtype='i4'
)

print(array_4byte)
print(array_4byte.dtype)
```

### Output:

```text
[1 2 3 4 5]
int32
```

چون:

```text
4 Byte = 32 Bit
```

پس:

```text
i4 → Integer → 4 Bytes → 32 Bits
```

---

# 6️⃣ String Size

برای String نیز می‌توانیم Size مشخص کنیم.

مثال:

```python
array_string = np.array(
    [1, 2, 3, 4, 5],
    dtype='S4'
)

print(array_string)
print(array_string.dtype)
```

اینجا:

```python
'S4'
```

یعنی String با ظرفیت 4 Byte برای هر عنصر.

---

# 7️⃣ dtype Structure

می‌توانیم `dtype` را به صورت زیر تصور کنیم:

```text
dtype
 │
 ├── Data Type
 │      │
 │      ├── i  → Integer
 │      ├── f  → Float
 │      ├── b  → Boolean
 │      └── S  → String
 │
 └── Size
        │
        ├── i4 → 4 Bytes
        ├── i8 → 8 Bytes
        └── S4 → 4 Bytes
```

مثلاً:

```python
dtype='i4'
```

یعنی:

```text
i  → Integer
4  → 4 Bytes
```

---

# 8️⃣ What if a Value Cannot Be Converted?

اگر Data Type مشخصی برای Array تعیین کنیم، NumPy تلاش می‌کند تمام عناصر را به همان نوع تبدیل کند.

مثلاً:

```python
arr = np.array(['x', 2, 5], dtype='i')
```

ما گفته‌ایم:

```python
dtype='i'
```

یعنی تمام عناصر باید Integer باشند.

اما:

```text
'x'
```

قابل تبدیل به Integer نیست.

بنابراین NumPy یک `ValueError` ایجاد می‌کند.

---

## Handling ValueError

می‌توانیم این خطا را با `try` و `except` مدیریت کنیم:

```python
def ValueError_test():
    try:
        arr = np.array(['x', 2, 5], dtype='i')
        return arr
    except ValueError:
        return "ValueError"


def ValueError_test_true():
    try:
        arr = np.array(['4', 2, 5], dtype='i')
        return "this is ok", arr
    except ValueError:
        return "ValueError"


print(ValueError_test())
print(ValueError_test_true())
```

### Output:

```text
ValueError
('this is ok', array([4, 2, 5], dtype=int32))
```

در مثال اول:

```python
'x'
```

قابل تبدیل به Integer نیست.

اما در مثال دوم:

```python
'4'
```

قابل تبدیل به Integer است.

پس:

```text
'x' → ❌ Integer
'4' → ✅ Integer
```

---

# 9️⃣ Converting Data Type on Existing Arrays

گاهی Array را قبلاً ساخته‌ایم و می‌خواهیم Data Type آن را تغییر دهیم.

برای این کار از:

```python
astype()
```

استفاده می‌کنیم.

`astype()` یک **Array جدید** با Data Type جدید ایجاد می‌کند.

مثال:

```python
first_array = np.array([
    1.1, 2.1, 3.4, 4.5, 5.8
])

new_array = first_array.astype('i')

print(first_array)
print(first_array.dtype)

print(new_array)
print(new_array.dtype)
```

### Output:

```text
[1.1 2.1 3.4 4.5 5.8]
float64

[1 2 3 4 5]
int32
```

در اینجا:

```python
first_array
```

همچنان `float` است و فقط `new_array` به `integer` تبدیل شده است.

---

# 🔟 astype('i') vs astype(int)

می‌توانیم Data Type را با Code یا Python Type مشخص کنیم:

```python
new_array = first_array.astype('i')
```

یا:

```python
new_array = first_array.astype(int)
```

هر دو برای تبدیل به Integer استفاده می‌شوند.

همین‌طور:

```python
astype('f')
```

یا:

```python
astype(float)
```

برای تبدیل به Float.

---

# 1️⃣1️⃣ Float to Integer

هنگام تبدیل Float به Integer، بخش اعشاری حذف می‌شود.

مثال:

```python
first_array = np.array([
    1.1, 2.1, 3.4, 4.5, 5.8
])

new_array = first_array.astype(int)

print(new_array)
```

### Output:

```text
[1 2 3 4 5]
```

یعنی:

```text
1.1 → 1
2.1 → 2
3.4 → 3
4.5 → 4
5.8 → 5
```

> 📌 در تبدیل Float به Integer، مقدار اعشاری نگه داشته نمی‌شود.

---

# 1️⃣2️⃣ Converting to Boolean

می‌توانیم یک Array را به Boolean نیز تبدیل کنیم:

```python
first_array = np.array([
    1.1, 0, 3.4, 4.5, 5.8
])

new_array = first_array.astype(bool)

print(new_array)
```

### Output:

```text
[ True False  True  True  True]
```

قاعده‌ی ساده:

```text
0       → False
non-zero → True
```

مثال:

```text
0   → False
1   → True
5   → True
-2  → True
```

---

# 1️⃣3️⃣ Complete Example

مثال زیر تمام مفاهیم اصلی این مرحله را کنار هم قرار می‌دهد:

```python
import numpy as np

first_array = np.array([
    1.1, 2.1, 3.4, 4.5, 5.8
])

def change_with_i(first_array):
    new_array = first_array.astype('i')

    print(
        f"first_array: {first_array} : {first_array.dtype}\n"
        f"new_array: {new_array} : {new_array.dtype}"
    )


def change_with_int(first_array):
    new_array = first_array.astype(int)

    print(
        f"first_array: {first_array} : {first_array.dtype}\n"
        f"new_array: {new_array} : {new_array.dtype}"
    )


print("change with (i):")
change_with_i(first_array)

print("\nchange with int:")
change_with_int(first_array)


first_array[1] = 0


def change_with_boolean(first_array):
    new_array = first_array.astype(bool)

    print(
        f"\nfirst_array: {first_array} : {first_array.dtype}\n"
        f"new_array: {new_array} : {new_array.dtype}"
    )


print("\nchange with bool:")
change_with_boolean(first_array)
```

---

# 🧠 Important Concept

دو روش اصلی برای تعیین Data Type داریم:

### هنگام ساخت Array:

```python
np.array([1, 2, 3], dtype='f')
```

یعنی از همان ابتدا Array را با نوع مشخص ایجاد کن.

### بعد از ساخت Array:

```python
arr.astype(float)
```

یعنی یک Array جدید با نوع داده‌ی جدید ایجاد کن.

پس:

```text
np.array(..., dtype=...)
        ↓
Define type when creating

astype(...)
        ↓
Convert an existing array
```

---

# 🧪 Exercises

### Exercise 1

یک Array شامل اعداد Float بسازید و آن را به Integer تبدیل کنید.

```python
arr = np.array([1.5, 2.8, 3.9])

# Your code
```

---

### Exercise 2

یک Array از Integer بسازید و آن را به Float تبدیل کنید.

```python
arr = np.array([1, 2, 3, 4])

# Your code
```

---

### Exercise 3

خروجی کد زیر را مشخص کنید:

```python
arr = np.array([0, 1, 5, -2])

print(arr.astype(bool))
```

---

### Exercise 4

کد زیر چرا `ValueError` ایجاد می‌کند؟

```python
arr = np.array(['hello', 2, 5], dtype='i')
```

---

# 📌 Important Notes

* `dtype` نوع داده‌ی عناصر Array را مشخص می‌کند.
* `dtype='i'` برای Integer استفاده می‌شود.
* `dtype='f'` برای Float استفاده می‌شود.
* `dtype='b'` برای Boolean استفاده می‌شود.
* `dtype='S'` برای Byte String استفاده می‌شود.
* `dtype='U'` برای Unicode String استفاده می‌شود.
* می‌توان Size را نیز مشخص کرد؛ مثلاً `i4`.
* `astype()` نوع داده‌ی یک Array موجود را تغییر می‌دهد.
* `astype()` یک Array جدید ایجاد می‌کند و Array اصلی را تغییر نمی‌دهد.
* تبدیل مقدار نامعتبر به یک Data Type می‌تواند باعث `ValueError` شود.
* هنگام تبدیل Float به Integer، بخش اعشاری حذف می‌شود.
* در Boolean، مقدار `0` برابر `False` و مقادیر غیر صفر برابر `True` هستند.

---

# 📝 Summary

در این مرحله با سیستم Data Type در NumPy آشنا شدیم.

مهم‌ترین مفاهیم:

```text
dtype
 ↓
Data Type of Array
```

```python
np.array([1, 2, 3], dtype='i')
```

برای تعیین نوع داده هنگام ساخت Array.

و:

```python
arr.astype(float)
```

برای تبدیل یک Array موجود به نوع داده‌ی جدید.

همچنین یاد گرفتیم که اگر مقدار قابل تبدیل نباشد:

```text
ValueError
```

ایجاد می‌شود.

---

## 🚀 Next Step

در مرحله بعد با **NumPy Array Copy vs View** آشنا می‌شویم و یاد می‌گیریم چرا تغییر یک Array گاهی روی Array دیگر نیز تأثیر می‌گذارد.
