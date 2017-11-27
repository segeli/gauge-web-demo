Modanisa Örnek Testleri
===========================

Örnek kullanıcı testlerinin yapılması gerekiyor

* "/"   adresine git

Kullanıcı başarılı giriş kontrol edilmeli
-------

tags: basariliLogin

* "headerLoginUrl" id nesnesi varsa tikla
* "phone" id nesnesine tikla
* "phone" id alanina "5425655252" yaz
* "password" id alanina "qzmqz7" yaz
* "#login-form > div:nth-child(8) > input" css nesnesine tikla
* ekranda "src sng" yazisini gormen gerekiyor



Kullanıcı hatalı giriş kontrol edilmeli
Basarili kullanıcı girişini hata olarak veren test
-------

tags: hataliGiris

* "headerLoginUrl" id nesnesi varsa tikla
* "phone" id nesnesine tikla
* "phone" id alanina "5425655252" yaz
* "password" id alanina "qzmqz7" yaz
* "#login-form > div:nth-child(8) > input" css nesnesine tikla
* ekranda "src sng123" yazisini gormen gerekiyor



Alısverisi Tamamla
---------

tags: alisverisiTamamla

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

tags: alısverisiTamamlama

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




