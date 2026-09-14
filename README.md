# 🧮 NumPy Learning Journey

<p align="center">
  <strong>A step-by-step journey to learn NumPy with Python</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-Learning-orange?style=flat-square&logo=numpy" alt="NumPy">
  <img src="https://img.shields.io/badge/Level-Beginner-green?style=flat-square" alt="Level">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square" alt="Status">
</p>

---

## 📖 درباره پروژه

این Repository یک مسیر آموزشی مرحله‌به‌مرحله برای یادگیری **NumPy** با زبان Python است.

این پروژه هم‌زمان با روند یادگیری ساخته می‌شود. هر موضوع ابتدا بررسی و یاد گرفته می‌شود، سپس مثال‌های عملی آن نوشته شده و در نهایت مطالب آموزشی و تمرین‌های مربوط به آن در Repository قرار می‌گیرند.

هدف این پروژه فقط یادگیری دستورات NumPy نیست؛ بلکه تلاش می‌کنیم مفاهیم را به‌صورت درست و قابل استفاده در پروژه‌های واقعی یاد بگیریم.

در هر مرحله، تمرکز اصلی روی سه موضوع است:

* درک مفهوم
* پیاده‌سازی با Python
* تمرین و تثبیت مطالب

> این Repository در طول مسیر تکمیل می‌شود و ساختار آموزشی آن نیز متناسب با روند یادگیری به‌روزرسانی خواهد شد.

---

## 🎯 هدف پروژه

هدف اصلی این پروژه، یادگیری NumPy از پایه و رسیدن به درک مناسبی از نحوه استفاده از آن در Python است.

در طول مسیر تلاش می‌کنیم علاوه بر یادگیری Syntax، با منطق و ساختار NumPy نیز آشنا شویم تا بتوانیم از آن در پروژه‌های آینده، به‌خصوص در حوزه‌هایی مانند:

* Data Analysis
* Data Science
* Machine Learning
* Scientific Computing

استفاده کنیم.

---

## 🗺️ مسیر یادگیری

مسیر این پروژه به‌صورت مرحله‌ای پیش می‌رود.

در حال حاضر سرفصل نهایی پروژه از قبل مشخص نشده است؛ زیرا موضوعات آموزشی را هم‌زمان با پیشرفت پروژه و بر اساس نیاز هر مرحله اضافه خواهیم کرد.

```text
Learning
   │
   ▼
Concept
   │
   ▼
Implementation
   │
   ▼
Practice
   │
   ▼
Review
   │
   ▼
Next Step
```

> هر مرحله را با هم کامل می‌کنیم و پس از پایان آن، مرحله بعدی به مسیر پروژه اضافه خواهد شد.

---

## 📚 منبع اصلی

منبع اصلی شروع این مسیر آموزشی:

**W3Schools — NumPy Tutorial**

[W3Schools — NumPy Tutorial](https://www.w3schools.com/python/numpy/?utm_source=chatgpt.com)

در صورت نیاز، در ادامه مسیر از مستندات رسمی NumPy و منابع معتبر دیگر نیز استفاده خواهیم کرد.

> هدف این Repository کپی کردن محتوای منابع نیست. مطالب با هدف یادگیری، تمرین و درک بهتر مفاهیم به زبان ساده‌تر نوشته می‌شوند.

---

## 🛠️ پیش‌نیازها

برای شروع این مسیر، آشنایی مقدماتی با Python پیشنهاد می‌شود.

بهتر است با مفاهیم زیر آشنا باشید:

* Variables
* Data Types
* Lists
* Tuples
* Dictionaries
* Sets
* `if / elif / else`
* `for`
* `while`
* Functions
* Basic Python Syntax

نیازی نیست در همه این مباحث حرفه‌ای باشید؛ آشنایی مقدماتی برای شروع کافی است.

---

## ⚙️ نصب و راه‌اندازی

### 1. Clone کردن Repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

سپس وارد پروژه شوید:

```bash
cd <PROJECT-NAME>
```

---

### 2. ساخت Virtual Environment

پیشنهاد می‌شود برای اجرای پروژه از محیط مجازی Python استفاده کنید:

```bash
python -m venv .venv
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

---

### 3. نصب NumPy

برای نصب NumPy:

```bash
pip install numpy
```

برای بررسی نصب:

```bash
python -c "import numpy; print(numpy.__version__)"
```

اگر نسخه NumPy نمایش داده شد، نصب با موفقیت انجام شده است.

---

## 📂 ساختار Repository

ساختار فعلی پروژه به شکل زیر است:

```text
learn_numpy/
│
├── README.md
│
├── requirements.txt
│
├── .gitignore
│
├── sessions/
│   │
│   ├── session_1/
│   │   ├── step_1.py
│   │   └── step_2.py
│   │
│   ├── session_2/
│   │   ├── step_1.py
│   │   └── step_2.py
│   │
│   ├── session_3/
│   │   ├── step_1.py
│   │   └── step_2.py
│   │
│   └── ...
│
└── Docs/
    │
    ├── session_1/
    ├── session_2/
    └── ...
```

### توضیح ساختار

| مسیر               | کاربرد                               |
| ------------------ | ------------------------------------ |
| `README.md`        | صفحه اصلی و معرفی پروژه              |
| `sessions/`        | کدهای مربوط به جلسات آموزشی          |
| `session_x/`       | فایل‌های یک جلسه مشخص                |
| `step_x.py`        | کد مربوط به هر مرحله                 |
| `Docs/`            | مستندات و توضیحات آموزشی             |
| `Docs/session_x/`  | مستندات مربوط به هر جلسه             |
| `requirements.txt` | وابستگی‌های پروژه                    |
| `.gitignore`       | فایل‌هایی که نباید در Git ذخیره شوند |

> ساختار پروژه در طول مسیر ممکن است با توجه به نیاز آموزش تغییر کند.

---

## 📌 روش مطالعه

این پروژه به‌صورت مرحله‌ای دنبال می‌شود.

برای هر مرحله ابتدا مفهوم را بررسی می‌کنیم، سپس آن را با Python پیاده‌سازی می‌کنیم و در ادامه با مثال و تمرین، موضوع را بهتر درک می‌کنیم.

الگوی کلی هر مرحله:

```text
Concept
   ↓
Explanation
   ↓
Code
   ↓
Output
   ↓
Important Notes
   ↓
Exercises
   ↓
Review
```

هدف این است که فقط کد را حفظ نکنیم؛ بلکه بدانیم:

> **چه چیزی را می‌نویسیم، چرا آن را می‌نویسیم و چه زمانی باید از آن استفاده کنیم.**

---

## 💡 فلسفه پروژه

این Repository یک پروژه آموزشی در حال توسعه است.

بنابراین قرار نیست از ابتدا تمام مسیر را مشخص کنیم.

هر مرحله بر اساس مرحله قبل ساخته می‌شود و مطالب جدید زمانی به پروژه اضافه می‌شوند که به آن‌ها برسیم.

سه سؤال اصلی در طول مسیر همیشه مورد توجه قرار می‌گیرند:

### 1. این چیست؟

ابتدا مفهوم را به‌درستی بشناسیم.

### 2. چرا به آن نیاز داریم؟

کاربرد و دلیل استفاده از آن را بفهمیم.

### 3. چگونه از آن استفاده کنیم؟

سپس مفهوم را با Python پیاده‌سازی کنیم.

---

## 📝 روش یادگیری

برای یادگیری بهتر، پیشنهاد می‌شود کدها فقط Copy/Paste نشوند.

بعد از یادگیری هر موضوع:

1. مثال را خودت اجرا کن.
2. کد را تغییر بده.
3. خروجی را بررسی کن.
4. مثال‌های مختلف بساز.
5. تمرین را بدون نگاه کردن به کد اصلی انجام بده.
6. در صورت امکان، یک مثال شخصی برای همان مفهوم بنویس.

> **اول مفهوم را بفهم، بعد کد را بنویس.**

---

## 📈 Progress

وضعیت پروژه در طول مسیر به‌روزرسانی خواهد شد.

```text
████░░░░░░░░░░░░░░░░ 20%
```

### Current Progress

| بخش          | وضعیت          |
| ------------ | -------------- |
| NumPy Basics | 🟢 In Progress |
| Next Steps   | ⚪ Not Started  |

> با کامل شدن هر مرحله، وضعیت این بخش نیز به‌روزرسانی خواهد شد.

---

## 🔗 منابع

### Main Resource

[W3Schools — NumPy Tutorial](https://www.w3schools.com/python/numpy/?utm_source=chatgpt.com)

### Official Documentation

[NumPy Documentation](https://numpy.org/doc/?utm_source=chatgpt.com)

### Python Documentation

[Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)

---

## 🤝 Contributing

این Repository در درجه اول یک مسیر یادگیری شخصی است.

با این حال، اگر اشتباهی در کد یا توضیحات مشاهده کردید، یا پیشنهادی برای بهتر شدن آموزش داشتید، می‌توانید از طریق `Issue` یا `Pull Request` آن را مطرح کنید.

---

## ⭐ Support

اگر این پروژه برای یادگیری NumPy برای شما مفید بود، می‌توانید با دادن یک ⭐ به Repository از ادامه این مسیر حمایت کنید.

---

## 📜 License

این پروژه با هدف آموزشی ساخته شده است.

مطالب آموزشی این Repository در طول مسیر یادگیری و با استفاده از منابع مختلف تهیه و تمرین می‌شوند. حقوق و شرایط استفاده از محتوای منابع خارجی تابع قوانین و مجوزهای همان منابع است.

---

<p align="center">
  Made with kyhvn(Zero) - Python and love❤️
</p>
