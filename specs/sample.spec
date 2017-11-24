Modanisa Örnek Testleri
===========================

Örnek kullanıcı testlerinin yapılması gerekiyor

* "/"   adresine git



//Ürün arama sonunda en az 5 ürün gelmeli
//Ürün arama
//---------
//
//
//
//* "search_word" id alanina "apple" yaz
//* "header_find_button" id nesnesine tikla
//* ekranda "bulundu" yazisini gormen gerekiyor
//
//Kategorilere girilebilmeli
//Kategori gezme
//------
//
//
//
//* "Menu-Banner" id nesnesi altindaki "Mod" yazisina tikla
//* ekranda "POPÜLER MARKALAR" yazisini gormen gerekiyor
//* "/"   adresine git
//* "Menu-Banner" id nesnesi altindaki "Elektronik" yazisina tikla
//* ekranda "Popüler Markalar" yazisini gormen gerekiyor


Kullanıcı başarılı giriş kontrol edilmeli
-------

Tags: basariliLogin

* "headerLoginUrl" id nesnesi varsa tikla
* "phone" id nesnesine tikla
* "phone" id alanina "5425655252" yaz
* "password" id alanina "qzmqz7" yaz
* "#login-form > div:nth-child(8) > input" css nesnesine tikla
* ekranda "src sng" yazisini gormen gerekiyor



Kullanıcı hatalı giriş kontrol edilmeli
Basarili kullanıcı girişini hata olarak veren test
-------

Tags: hataliGiris

* "headerLoginUrl" id nesnesi varsa tikla
* "phone" id nesnesine tikla
* "phone" id alanina "5425655252" yaz
* "password" id alanina "qzmqz7" yaz
* "#login-form > div:nth-child(8) > input" css nesnesine tikla
* ekranda "src sng123" yazisini gormen gerekiyor



Alısverisi Tamamla
---------

Tags: alisverisiTamamla

*  "sercan.sengoz@sahabt.com" ve "qzmqz7" ile giris yap
*  "rootItem" class'li eleman listesindenden rastgele birine tıkla
* "productsItem" class'li eleman listesindenden rastgele birine tıkla
* "#size-box-container a" css'li eleman listesindenden rastgele birine tıkla
* "addtobasket" id nesnesine tikla
* "cart" id'li elemana mouse u hareket ettir
* "btn-checkout" className nesnesine tikla
* "buy-button2" className nesnesine tikla
* "cargoCompanyId-1" id nesnesine tikla
* "address-confirm-button" id nesnesine tikla
* "#cod-form > label > div.payment-radio > input" css nesnesine tikla
* "term" id'li elemanın koordinatlarında sayfada scroll işlemi yap
* "term" id nesnesine tikla
* "#cod-form > div > input" css nesnesine tikla


Alısverisi Tamamlama
---------

Tags: alisverisiTamamlama

*  "sercan.sengoz@sahabt.com" ve "qzmqz7" ile giris yap
*  "rootItem" class'li eleman listesindenden rastgele birine tıkla
* "productsItem" class'li eleman listesindenden rastgele birine tıkla
* "#size-box-container a" css'li eleman listesindenden rastgele birine tıkla
* "addtobasket" id nesnesine tikla
* ekranda "src sng123" yazisini gormen gerekiyor
* "cart" id'li elemana mouse u hareket ettir
* "btn-checkout" className nesnesine tikla
* "buy-button2" className nesnesine tikla
* "cargoCompanyId-1" id nesnesine tikla
* "address-confirm-button" id nesnesine tikla
* "#cod-form > label > div.payment-radio > input" css nesnesine tikla
* "term" id'li elemanın koordinatlarında sayfada scroll işlemi yap
* "term" id nesnesine tikla
* "#cod-form > div > input" css nesnesine tikla




