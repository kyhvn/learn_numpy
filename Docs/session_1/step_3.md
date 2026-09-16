# 📘 Session 1 — Step 3: Slicing Arrays

در این مرحله یاد می‌گیریم چگونه با استفاده از `Slicing` بخشی از عناصر یک `NumPy Array` را انتخاب کنیم.

---

## 🎯 هدف این مرحله

در این مرحله با مفاهیم زیر آشنا می‌شویم:

- `Array Slicing`
- ساختار `[start:stop:step]`
- `start`, `stop`, `step`
- Slicing در آرایه‌های یک‌بعدی
- `Negative Slicing`
- Slicing در آرایه‌های دوبعدی

---

# 1. What is Slicing?

در Python، `Slicing` یعنی انتخاب تعدادی از عناصر آرایه از یک محدوده مشخص.

ساختار Slicing به شکل زیر است:

```python
array[start:stop:step]
```

یعنی:

```text
[start : stop : step]
    ↓      ↓      ↓
  شروع    پایان   گام
```

نکته مهم:

- `start` شامل می‌شود.
- `stop` شامل نمی‌شود.
- `step` فاصله حرکت را مشخص می‌کند.

اگر مقدارها را مشخص نکنیم:

```text
start → 0
stop  → طول آرایه
step  → 1
```

---

# 2. Creating a NumPy Array

ابتدا یک `List` ایجاد کرده و آن را به `NumPy Array` تبدیل می‌کنیم:

```python
import numpy as np

a_list = [1,2,3,4,5,6,7,8,9,10]
a_array = np.array(a_list)
```

ساختار آرایه:

```text
Index:    0  1  2  3  4  5  6  7  8  9
Value:    1  2  3  4  5  6  7  8  9  10
```

---

# 3. Basic Slicing

### Start, Stop and Step

```python
sliced_array1 = a_array[0:5:2]

print(sliced_array1)
```

خروجی:

```text
[1 3 5]
```

چون:

```text
0 → 1
2 → 3
4 → 5
```

و `Index 5` شامل نمی‌شود.

---

### Start and Stop

اگر `step` را مشخص نکنیم، مقدار آن `1` است:

```python
sliced_array2 = a_array[3:7]

print(sliced_array2)
```

خروجی:

```text
[4 5 6 7]
```

---

# 4. Slicing Without Start

اگر `start` را مشخص نکنیم، از Index `0` شروع می‌شود.

```python
sliced_array4 = a_array[:5]

print(sliced_array4)
```

این کد معادل است با:

```python
a_array[0:5:1]
```

خروجی:

```text
[1 2 3 4 5]
```

---

# 5. Slicing Without Stop

اگر `stop` را مشخص نکنیم، تا انتهای آرایه ادامه پیدا می‌کند.

```python
sliced_array3 = a_array[5:]

print(sliced_array3)
```

خروجی:

```text
[ 6  7  8  9 10]
```

---

# 6. Slicing With Step

می‌توانیم فقط `step` را مشخص کنیم:

```python
sliced_array6 = a_array[::2]

print(sliced_array6)
```

یعنی از ابتدا شروع کن و با فاصله `2` حرکت کن.

خروجی:

```text
[1 3 5 7 9]
```

---

# 7. Negative Slicing

در Slicing می‌توانیم از Indexهای منفی نیز استفاده کنیم.

```text
Value:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Negative Index:
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
```

مثلاً:

```python
sliced_array5 = a_array[-1:-6:-2]

print(sliced_array5)
```

یعنی:

```text
Start → -1
Stop  → -6
Step  → -2
```

حرکت:

```text
-1 → 10
-3 → 8
-5 → 6
```

خروجی:

```text
[10 8 6]
```

---

# 8. Slicing 2D Arrays

برای آرایه‌های دوبعدی می‌توانیم هم `Row` و هم `Column` را Slice کنیم.

ساختار:

```python
array[row_slice, column_slice]
```

مثلاً:

```python
b_array = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
```

ساختار آرایه:

```text
          Column
          0  1  2  3
        ──────────────
Row 0   [1  2  3  4]
Row 1   [5  6  7  8]
```

---

## Slicing یک Row

برای انتخاب عناصر `6` و `7`:

```python
print(b_array[1, 1:3])
```

ابتدا:

```text
Row 1 → [5,6,7,8]
```

سپس:

```text
Column 1 → 6
Column 2 → 7
```

خروجی:

```text
[6 7]
```

---

## Slicing چند Row و Column

```python
print(b_array[0:2, 2:4])
```

یعنی:

```text
Rows    → 0:2
Columns → 2:4
```

خروجی:

```text
[[3 4]
 [7 8]]
```

---

# 9. Question

به خروجی این کد دقت کنید:

```python
print(b_array[0:2, 2])
```

آرایه:

```text
          0  1  2  3
        ──────────────
Row 0   [1  2  3  4]
Row 1   [5  6  7  8]
```

ما داریم:

```text
Rows    → 0:2
Column  → 2
```

پس:

```text
Row 0 → 3
Row 1 → 7
```

خروجی:

```text
[3 7]
```

اما اگر بنویسیم:

```python
print(b_array[0:2, 2:3])
```

خروجی:

```text
[[3]
 [7]]
```

تفاوت مهم:

```python
b_array[0:2, 2]
```

یک `Column` را انتخاب می‌کند.

اما:

```python
b_array[0:2, 2:3]
```

یک `Slice` از `Column` را انتخاب می‌کند و ساختار دوبعدی را حفظ می‌کند.

---

# 📌 Important Notes

- ساختار اصلی Slicing:

```python
[start:stop:step]
```

- `start` شامل می‌شود.
- `stop` شامل نمی‌شود.
- مقدار پیش‌فرض `step` برابر `1` است.
- `array[:5]` از ابتدا تا قبل از Index `5` است.
- `array[5:]` از Index `5` تا انتها است.
- `array[::2]` عناصر یکی در میان را انتخاب می‌کند.
- `step` منفی باعث حرکت از انتهای آرایه به سمت ابتدا می‌شود.
- در آرایه دوبعدی:

```python
array[row, column]
```

- برای Slicing در آرایه دوبعدی:

```python
array[row_slice, column_slice]
```

---

# 🧪 Exercises

## تمرین 1

با استفاده از آرایه زیر، اعداد `20` تا `50` را انتخاب کنید:

```python
array = np.array([10,20,30,40,50,60])
```

خروجی:

```text
[20 30 40 50]
```

---

## تمرین 2

با استفاده از `Negative Slicing` سه عنصر آخر را انتخاب کنید:

```python
array = np.array([10,20,30,40,50,60])
```

---

## تمرین 3

آرایه زیر را برعکس کنید:

```python
array = np.array([1,2,3,4,5])
```

خروجی:

```text
[5 4 3 2 1]
```

---

## تمرین 4

در آرایه زیر خروجی زیر را ایجاد کنید:

```python
array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
```

خروجی:

```text
[[2 3]
 [5 6]]
```

---

# 📝 Summary

در این مرحله با `Slicing` در NumPy آشنا شدیم.

ساختار اصلی:

```python
[start:stop:step]
```

در آرایه‌های دوبعدی:

```python
array[row_slice, column_slice]
```

مثال:

```python
a_array[0:5:2]
```

یعنی:

```text
Start → 0
Stop  → 5
Step  → 2
```

و:

```python
b_array[0:2, 2:4]
```

یعنی:

```text
Rows    → 0:2
Columns → 2:4
```

### نکته کلیدی

> **Slicing یعنی انتخاب بخشی از عناصر آرایه با استفاده از Start، Stop و Step.**

---

## 🚀 Next Step

در مرحله بعد با مفهوم جدیدی از `NumPy Arrays` آشنا می‌شویم و آن را با مثال و تمرین یاد می‌گیریم.