# Python String metodlari

| Metod         | Nima vazifa qiladi                  | Parametrlari           | Misol                         | Natija         |
|---------------|-------------------------------------|-------------------------|-------------------------------|----------------|
| `capitalize()`| Birinchi harfni katta qiladi        | -                       | `'salom'.capitalize()`        | `'Salom'`      |
| `casefold()`  | Katta harflarni kichik qiladi       | -                       | `'ÖZBEK'.casefold()`          | `'ozbek'`      |
| `center()`    | Markazga joylashtiradi              | `width: int`            | `'hi'.center(6)`              | `'  hi  '`     |
| `count()`     | Belgilar sonini sanaydi             | `sub: str`              | `'banana'.count('a')`         | `3`            |
| `encode()`    | Baytga o‘tkazadi                    | `encoding='utf-8'`      | `'salom'.encode()`            | `b'salom'`     |
| `endswith()`  | Tugashini tekshiradi                | `suffix: str`           | `'salom'.endswith('lom')`     | `True`         |
| `expandtabs()`| `\t` ni bo‘shliqqa aylantiradi      | `n: int`                | `'1\\t2'.expandtabs(4)`       | `'1   2'`      |
| `find()`      | Belgining pozitsiyasini topadi      | `s: str`                | `'banana'.find('na')`         | `2`            |
| `format()`    | Matnga qiymat joylaydi              | `qiymatlar`             | `'Salom, {}'.format('Ali')`   | `'Salom, Ali'` |
| `index()`     | Xatolik bilan qidiradi              | `s: str`                | `'banana'.index('na')`        | `2`            |
| `isalnum()`   | Harf yoki raqamdan iboratmi         | -                       | `'abc123'.isalnum()`          | `True`         |
| `isalpha()`   | Faqat harflardan iboratmi           | -                       | `'abc'.isalpha()`             | `True`         |
| `isdigit()`   | Faqat raqamlardan iboratmi          | -                       | `'42'.isdigit()`              | `True`         |
| `islower()`   | Hammasi kichikmi                    | -                       | `'hello'.islower()`           | `True`         |
| `isupper()`   | Hammasi katta harfmi                | -                       | `'HELLO'.isupper()`           | `True`         |
| `join()`      | Elementlarni birlashtiradi          | `iterable`              | `'-'.join(['a','b'])`         | `'a-b'`        |
| `ljust()`     | Chapga joylaydi                     | `width: int`            | `'hi'.ljust(5)`               | `'hi   '`      |
| `lower()`     | Kichik harfga aylantiradi           | -                       | `'HELLO'.lower()`             | `'hello'`      |
| `replace()`   | Belgini almashtiradi                | `old, new`              | `'hello'.replace('l','r')`    | `'herro'`      |
| `rfind()`     | Oxirgi pozitsiyani topadi           | `s: str`                | `'banana'.rfind('na')`        | `4`            |
| `rjust()`     | O‘ngga joylaydi                     | `width: int`            | `'hi'.rjust(5)`               | `'   hi'`      |
| `rsplit()`    | Orqadan bo‘lib ajratadi             | `sep, maxsplit`         | `'a,b,c'.rsplit(',', 1)`      | `['a,b', 'c']` |
| `split()`     | Bo‘lib listga o‘tkazadi             | `sep: str`              | `'a,b,c'.split(',')`          | `['a', 'b', 'c']` |
| `startswith()`| Boshlanishini tekshiradi            | `s: str`                | `'hello'.startswith('he')`    | `True`         |
| `strip()`     | Bo‘sh joylarni olib tashlaydi       | -                       | `'  hi  '.strip()`            | `'hi'`         |
| `swapcase()`  | Harflar registrini almashtiradi     | -                       | `'PyThOn'.swapcase()`         | `'pYtHoN'`     |
| `title()`     | Har so‘zni bosh harf bilan yozadi   | -                       | `'hello world'.title()`       | `'Hello World'`|
| `upper()`     | Katta harfga aylantiradi            | -                       | `'hello'.upper()`             | `'HELLO'`      |
| `zfill()`     | Boshi 0 bilan to‘ldiriladi          | `width: int`            | `'42'.zfill(5)`               | `'00042'`      |
