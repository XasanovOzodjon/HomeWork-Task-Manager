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

# Python List metodlari

| Metod         | Nima vazifa qiladi                            | Parametrlari                     | Misol                           | Natija                     |
|---------------|-----------------------------------------------|----------------------------------|---------------------------------|----------------------------|
| `append()`    | Oxiriga element qo‘shadi                      | `element`                        | `a = [1, 2]; a.append(3)`       | `[1, 2, 3]`                |
| `clear()`     | Barcha elementlarni o‘chiradi                 | -                                | `a = [1, 2]; a.clear()`         | `[]`                       |
| `copy()`      | Ro‘yxatdan nusxa oladi                        | -                                | `b = a.copy()`                  | `b = [1, 2]`               |
| `count()`     | Belgilangan element necha marta borligini topadi | `element`                     | `[1, 2, 2, 3].count(2)`         | `2`                        |
| `extend()`    | Boshqa ro‘yxat elementlarini qo‘shadi         | `iterable`                       | `a = [1]; a.extend([2, 3])`     | `[1, 2, 3]`                |
| `index()`     | Elementning birinchi indeksini topadi         | `element`                        | `[1, 2, 3].index(2)`            | `1`                        |
| `insert()`    | Belgilangan indeksga element qo‘shadi         | `index, element`                 | `a = [1, 3]; a.insert(1, 2)`    | `[1, 2, 3]`                |
| `pop()`       | Oxirgi yoki ko‘rsatilgan elementni chiqaradi  | `index (ixtiyoriy)`              | `[1, 2, 3].pop()`               | `3`, `[1, 2]`              |
| `remove()`    | Belgilangan qiymatdagi elementni o‘chiradi    | `element`                        | `a = [1, 2]; a.remove(2)`       | `[1]`                      |
| `reverse()`   | Elementlar tartibini teskarisiga o‘zgartiradi | -                                | `a = [1, 2]; a.reverse()`       | `[2, 1]`                   |
| `sort()`      | Elementlarni tartiblaydi                      | `key=None, reverse=False`        | `a = [3, 1, 2]; a.sort()`       | `[1, 2, 3]`                |


