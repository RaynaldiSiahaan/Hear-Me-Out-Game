define h = Character("Hana")
define k = Character("Pak Joko")
define r = Character("Rudi")
define i = Character("Bully 1")
define j = Character("Bully 2")
define dis = { "master" : Dissolve(0.3) }
define pushright = PushMove(0.5, "pushright")
define pushleft = PushMove(0.5, "pushleft")
define pushup = PushMove(0.5, "pushup")
define pushdown = PushMove(0.5, "pushdown")
define pixelate = Pixellate(0.3, "pixelate")
label start:

    $ emosi = 0
    scene its
    play music "audio/Upbeat and Happy Background Music.mp3"
    pause
    $ y = renpy.input("Siapa namamu?")
    if y == "":
        "Beritahu kami namamu"
    "Halo [y], selamat bermain"
    pause
    show rudi with dis
    r "Wah, gak nyangka semester ini selesai juga, gak sabar liburan."
    menu:
         "Haha, tinggal nunggu hadiah dari pak dosen":
            hide rudi
            show rudismug
            r "Wah, iya dong, ketua kelas IPnya pasti tinggi"


         "Waduh, gatau deh nilai aku bakalan gimana":
            hide rudi
            show rudismug
            r "Jangan merendah, pasti kamu bakalan dapat top 3 lagi"




    y "Yaa... lihat saja besok"
    hide rudismug
    show rudikaget
    r "Oh iya, Hana sudah seminggu gak masuk kelas, tumben banget, padahal biasanya dia yang paling aktif"

    menu:
         "Paling besok juga datang":
             hide rudi
             show rudisenyum
             r "Iya dong murid kebanggaan kelas"
         "Kalau ada hadiah juga dia datang":
             hide rudi
             show rudisenyum
             r "Hahaha, hadiahnya lumayan sih"

    scene hitam
    "Keesokan harinya..."

    scene kelas
    show rudi
    r "[y], gimana udah lihat hasil belum?"

    menu:
          "Udah dong":
             hide rudi
             show rudisenyum
             r "Percaya diri sekali kamu ya"
          "Auto dapat hadiah":
             hide rudi
             show rudisenyum
             r "Percaya diri sekali kamu ya"
    hide rudisenyum
    show rudi
    r "Eh, Hana udah datang tuh, tapi tumben diem amat, dia kenapa sih jadi aneh?"
    scene kelas
    show crimminormal with dis
    h ". . ."
    menu:
        "Kenapa ya? Aku coba ajak ngomong dulu ya":
            hide crimminormal
            show rudi
            r "Okay, semangat"
            jump script1
        "Gak usah deh, bukan urusan kita":
            $ emosi +=1
            jump script2

    label script1:
        scene kelas
        show crimminormal with dissolve
        h "?"
        y "Pagi Hana"
        hide crimminormal
        show crimmisenyum
        h "Pagi"
        menu:
            "Kamu kenapa kok kayak murung gitu":
                 jump script3
            "Gak datang seminggu, ngapain aja kamu":
                 jump script4
                 $ emosi += 1





    label script2:
        scene kelas
        show rudikasihan with dis
        r "Iya ya, ganggu kutu buku nanti malah digigit"
        hide rudikasihan
        show rudikaget
        r "Eh, pak dosen udah masuk, balik ke tempat duduk gih"
        jump lanjut

    label script3:
        scene kelas
        hide crimmisenyum
        show crimminormal
        h "Engga, aku gak apa-apa kok, kamu kembali duduk aja, pak dosen udah mau datang"
        y "Apa ada sesuatu yang terjadi? Kamu akhir-akhir ini sering bolos dan tidak aktif di grup chat"
        hide crimminormal
        show crimmisenyum
        h "Gapapa kok, bisa tinggalin aku sendiri saja"
        menu:
            "Kalau ada yang sedang mengganggu pikiranmu, kamu bisa cerita padaku":
                h "Iya, tenang saja"
                jump lanjut
            "Okay, aku duluan ya":
                hide crimmisenyum
                show crimminormal
                h "Dadah"
                jump lanjut

    label script4:
        scene kelas
        hide crimmisenyum
        show crimminormal
        h "Iya, aku belakangan ini agak sibuk"
        y "Sibuk apa sampai bolos seminggu? Gak pernah muncul di grup chat lagi, habis dari gua?"
        hide crimminormal
        show crimminormalbuka
        h "Apaan sih"
        y "Hahaha, aku hanya bercanda, jangan baper dong."
        y "Tapi serius kamu kemana deh"
        hide crimminormalbuka
        show crimminormal
        h "Udah, duduk aja, pak dosen sudah datang"
        jump lanjut

    label lanjut:
        stop music fadeout 1.0
        scene hitam
        "Setelah kelas berakhir..."
        scene its
        play music "audio/Once Upon a Time Storytelling for Children, Slow Guitar Songs for Fairy Tales and Fantasy Storie.mp3"
        show rudipenasaran with dissolve
        r "Eh, kamu gak sadar ada hal yang aneh?"
        menu:
            "Hal aneh apa?":
                r "Itu loh, tumben semester ini Hana gak dapat hadiah"
            "Gak ada hal aneh kok":
                r "Ah, gak peka banget kamu, lihat tuh masa Hana gak dapat hadiah"

        hide rudipenasaran
        show rudikaget
        r "Eh, itu Hana lagi bicara sama pak dosen, yuk coba kita lihatin"
        hide rudikaget with dissolve
        pause
        scene lapangan with pushright
        "Kamu mendengar Hana diberi peringatan keras oleh dosen, ternyata nilainya turun secara drastis"
        show crimmikecewa with dissolve
        h "Maafkan saya pak"
        hide crimmikecewa
        show rudikasihan
        r ". . . "
        y ". . ."

        scene black with fade
        "Libur telah berakhir, saatnya menyambut semester baru, semua mahasiswa terlihat bersemangat, kecuali seseorang"

        scene its with fade
        show bulli1 with dissolve
        i "Ehh Hana ternyata masuk, tubuhnya kurus banget ya, seperti tengkorak berjalan"
        show bulli2 with dis
        j "Hahahaha"
        show crimmi with dis
        h "..."
        i "Pinter pinter kok bisa dapat sampai IP 1,8 ya"
        j "Bosen pintar kali"
        i "HAHAHA... bisa-bisanya, padahal matamu sayu seperti gak tidur 2 minggu"
        hide crimmi
        show crimmimarah
        h "Tinggalin aku sendiri aja"
        j "Ihhh berani jawab ya"
        i "Hahaha, udah lah kita tinggalin aja, jangan dekat dekat entar ikutan jadi urakan karena keseringan belajar"
        j "Iya bener banget, jangan sampai aku kayak dia deh"

        scene hitam with dissolve
        pause

        scene kelas with dissolve
        y "HANAA ! Aku senang kamu masuk di hari pertama"
        show crimmi with dissolve
        h "Ahh iya"
        y "Haa aku tau, kamu pasti sangat bersemangat ya karena kelas hari ini ada dosen favoritmu"
        h "Nggak juga"
        menu:
            "Pasti kamu sudah tidak sabar belajar":
                hide crimmi
                show crimmibuka
                h "Apa gunanya belajar kalau aku terlihat seperti orang gila"
            "Waduh, Hana yang rajin belajar mulai jadi malas ya, parah nih":
                $ emosi += 1
                hide crimmi
                show crimmikecewa
                h "Memang lebih baik malas aja ya"
        y "Kok gitu ?"

        scene its with dissolve
        show rudikaget with dissolve
        r "Jadi bagaimana pendapatmu tentang Hana?"
        menu:
            "Nggak kayak biasanya, Hana kan orangnya ceria":
                r "Dia benar-benar berubah"
            "Agak aneh sih, biasa Hana orangnya termotivasi":
                r "Dia benar-benar berubah"
        y "Berubah karena apa?"
        hide rudikaget
        show rudipenasaran
        r "Yaa, mungkin karena salah pergaulan makanya akhir-akhir ini dia jadi sangat sensitif"
        hide rudipenasaran
        show rudismug
        r "Dia juga cemberut terus, pantes semua jadi menjauhi dia"

        menu:
            "Jangan berasumsi seperti itu":
                jump script5
            "Ah benar juga ya, itu bisa saja terjadi":
                jump script6

    label script5:
        scene its
        hide rudismug
        show rudisenyum
        r "Kamu tidak lihat memang, semua menghindari Hana"
        hide rudisenyum
        show rudikecewa
        r "Aku bahkan pernah dengar kalo dia dibully dan jadi gila, pokoknya kita jauh-jauh aja dari dia"
        menu:
            "Jangan seperti itu, Hana juga teman kita":
                jump script7
            "Hmmm, dia memang seperti gak terima bantuan sih, abaikan saja":
                jump script8

    label script6:
        scene its
        hide rudismug
        show rudi
        r "Iya makanya gaperlu ikutin deh"
        jump lanjutan2

    label script7:
        scene its
        hide rudi
        show rudikaget
        r "[y], kamu tidak pernah dengar ya, katanya orang bisa tiba-tiba sakit atau menjadi gila karena dipengaruhi setan"
        r "Kamu mau ikut tertular gila?"
        menu:
         "Itu hanya takhayul":
             hide rudikaget
             show rudipenasaran
             r "Takhayul gimana?"
             y "Bisa saja dia mengalami gangguan dalam hidupnya"
             y "Kita tidak boleh berpikir macam-macam"
         "Kamu sudah kelewatan":
             hide rudikaget
             show rudikasihan
         r "Iya iya deh, maaf"
        y "Aku harus bicara lagi dengan Hana"
        jump lanjutan2

    label script8:
        scene its
        hide rudismug
        show rudi
        r "Iya kan, lebih baik kita jauhin saja, nanti ikutan gila"
        y ". . ."
        jump lanjutan2

label lanjutan2:
    scene lorong
    y "Hana"
    show crimmibuka with dissolve
    h "Ya?"
    y "Kamu dari tadi hanya diam di kelas"
    hide crimmibuka
    show crimmi
    h "Iya, lagi mager ngomong aja"
    y "Bagaimana dengan kabarmu akhir-akhir ini, selama liburan kamu tidak pernah menghubungiku"
    h "Ya begitulah, tidak ada yang istimewa"
    menu:
         "Hana, jujur dong, sebenarnya ada apa sih?":
            $ emosi += 1
            hide crimmi
            show crimmikecewa
            h "Kamu mau apa sih, kenapa seperti menginterogasiku."
            y "Bukan begitu, aku hanya ingin tau kabarmu saja"
            hide crimmikecewa
            show crimmibuka
            h "Cukup, aku tidak ingin membahas soal itu"
            hide crimmi with moveoutleft
            jump a1

         "Hana, kamu bisa cerita dengan aku kok.":
             hide crimmi
             show crimmikecewa
             h "Apa dengan bercerita masalah itu akan selesai"
             y "Hana..."
             hide crimmikecewa
             show crimmisenyum
             h "Tidak apa - apa, bukanlah sesuatu yang harus dipikirkan."
             jump a1

    label a1:
    scene its with fade
    y "Sepertinya terjadi kesalahpahaman antara aku dengan Hana."
    y "Ahh, aku jadi mengacaukannya"
    show rudikecewa with dis
    r "Kenapa sih kamu sangat memperdulikan Hana, kenapa tidak biarkan saja."
    r "Dia juga sudah  menyuruhmu jangan ikut campur"
    menu:
         "Hana dalam masalah, kita harus membantunya":
            y "Menghindari bahkan sampai mengintimidasi seperti itu hanya akan memperburuk keadaan"
         "Setidaknya dengan mendengarkan kita dapat membantunya":
            y "Menghindari bahkan sampai mengintimidasi seperti itu hanya akan memperburuk keadaan"
    hide rudikecewa
    show rudikasihan
    r "Benar juga, aku jadi merasa bersalah kepada Hana"
    y "Ahh, aku jadi kepikiran sesuatu, coba ikut aku"
    hide rudikasihan
    show rudipenasaran
    r "Kemana?"
    hide rudipenasaran


    scene rumah with pushright
    pause
    show rudipenasaran with dissolve
    r "Bukannya ini rumah Hana?"
    y "Iya, aku mau minta maaf soal yang tadi, jadi aku bisa menjelaskan niatku untuk membantunya"
    r "Baiklah, kali ini aku akan mendukungmu"
    hide rudipenasaran
    show rudikasihan
    r "Tapi... Hana sepertinya tidak ada di rumah"
    menu:
        "Pintunya tidak dikunci, langsung masuk saja":
            hide rudikasihan
            show rudi
            r "Okei, tetap berhati-hati"
        "Jendelanya terbuka, kita dari jendela saja":
            hide rudikasihan
            show rudikaget
            r "Kamu pikir kita maling? Pintunya tidak dikunci, lebih baik lewat pintu saja"
    scene back
    show rudipenasaran
    r "Jadi kita mau ngapain disini?"
    y "Mungkin kita bisa cari petunjuk dari sini"
    hide rudipenasaran with dissolve
    "Carilah sebuah potongan kertas"

    call screen Test

    label lanjoet:
    scene back
    y "Rudi, lihat!"
    show rudikaget with dis
    r "Depresi ?! Jadi memang dia..."
    y "Dia memang dalam masa yang sulit"
    r "Ini beneran??"


    show crimmi2 with moveinright
    h "Kalian sedang apa? Kenapa kalian sembarangan menyelinap rumahku?"
    hide rudikaget
    show rudi2
    menu:
        "Bukan begitu, kami hanya melihat-lihat saja":
            h "Melihat-melihat apa, kalian masuk rumahku tanpa izin dan dengan lancang melihat barangku"
            hide crimmi2
            show crimmi1
            h "Apa kalian sebegitu ingin tahunya kalau aku benar-benar jadi gila hah!"
            jump b4

        "Ngapain harus ngamuk sih":
            $ emosi += 1
            if emosi >= 3:
                scene rudimarah
                show rudi
                r "Bentar-bentar"
                hide rudi
                show rudipenasaran with pixellate
                r "Kamu yakin mau pilih itu?"
                hide rudipenasaran
                show rudikecewa with pixellate
                r "Kamu sudah melakukan cukup banyak kesalahan loh"
                hide rudikecewa
                show rudingamok
                r "Kalau kamu pilih itu, aku gabakal tanggungjawab sama apa yang terjadi selanjutnya"
                r "Jadi gimana, masih mau pilihan itu?"
                menu:
                    "Iya":
                        hide rudingamok
                        show rudi
                        r "Baiklah kalau itu maumu"
                        hide rudi with fade
                        jump b1

                    "Tidak":
                        hide rudingamok
                        show rudi
                        r "Pilihan bagus"
                        hide rudi with fade
                        scene back
                        show crimmi2
                        menu:
                         "Bukan begitu, kami hanya melihat-lihat saja":
                            h "Melihat-lihat apa, kalian masuk rumahku tanpa izin dan dengan lancang melihat rekam medis ini"
                            h "Apa kalian sebegitu ingin tahunya kalau aku benar-benar jadi gila hah!"
                            jump b4

                if emosi < 3:
                    jump b1
    label b1:
    scene back
    show rudi2
    show crimmi2
    h "Tentu saja aku harus marah, kalian masuk rumahku tanpa izin dan dengan lancang melihat rekam medis ini"

    h "Kalian benar benar ingin tahu kalau aku gila ya!"
    jump b4

    label b4:

    r "Hana, itu bukan seperti yang kamu pikirkan, kami bukannya sengaja-"
    hide crimmi2
    show crimmi1 with vpunch
    h "Keluar dari rumahku sekarang! Cepat keluar!!"
    jump hm

    label hm:
    scene its with fade
    show rudikasihan
    pause
    r "Bagaimana ini [y]"
    menu:
        "Ya sudahlah, mau bagaimana lagi, kita hanya memperburuk keadaan":
            hide rudikasihan
            show rudikecewa
            r "Wah langsung nyerah ini, tadi kamu yang semangat"
        "Padahal aku ingin meluruskan masalah, malah jadi kacau":
            hide rudikasihan
            show rudikaget
            r "Iya, kesalahan kita juga sih"
    hide rudikasihan
    show rudikaget
    r "Tapi, apa separah itu ya terkena depresi sampai dia minum obat"
    menu:
        "Apa semua itu karena dia depresi?":
            hide rudikaget
            show rudipenasaran
            r "Bisa jadi sih"
        "Masa sih karena depresi bisa sampai begitu?":
            hide rudikaget
            show rudipenasaran
            r "Yaa.. itu hanya perkiraan saja"
        "Gak mungkin karena depresi bisa gini":
            hide rudikaget
            show rudipenasaran
            r "Mungkin saja itu sudah terlalu berat untuknya"

    r "Lagipula, depresi merupakan hal yang biasa di lingkungan mahasiswa, kebanyakan orang juga rasanya pernah depresi"
    y "Lebih baik kita coba tanyakan kepada psikolog sekolah kita"

    scene psikolog
    pause
    show rudi
    r "Selamat pagi pak"
    scene psikolog
    show sergei
    k "Selamat pagi, ada yang bisa saya bantu?"
    menu:
        "Saya ingin bertanya perihal teman saya":
         k "Iya silahkan, kamu bisa tanya apapun jika itu perihal kesehatan jiwa karena saya adalah seorang psikolog"
    r "Jadi begini pak, teman saya didiagnosis mengalami depresi dan diberi obat-obatan"
    menu:
        "Jika dia depresi apakah harus minum obat?":
         k "Tidak juga, obat yang diberikan biasanya hanya bersifat anti-depressan agar emosinya dapat dikontrol."
         k "Namun, obat-obatan ini bukan satu-satunya jalan."
         k "Bagi orang yang mengalami depresi dan telah berkunjung ke psikiater, tetap saja perlu motivasi dari diri sendiri untuk mau berubah"
    menu:
        "Apakah depresi itu sama seperti orang gila, atau berpotensi?":
         hide sergei
         show sergeibuka
         k "Tentu saja tidak, tidak semua orang yang memiliki gangguan jiwa adalah orang gila, itu merupakan perspektif yang salah di masyarakat."
         hide sergeibuka
         show sergei
         k "Istilah medis yang lebih tepat untuk kasus tersebut adalah Orang Dengan Gangguan Jiwa atau yang kita sebut dengan ODGJ"
    menu:
        "Bukankah stres dan depresi adalah hal biasa? Tapi kenapa sampai memerlukan obat?":
         hide sergei
         show sergeibuka
         k "Stres dan depresi adalah dua hal yang berbeda."
         k "Stres memang hal yang biasa dialami dimana manusia bereaksi terhadap sesuatu yang dia rasa sulit atau takuti yang menyebabkan rasa cemas dan khawatir."
         hide sergeibuka
         show sergei
         k "Depresi adalah tingkat lebih lanjut dari stres."
         k "Depresi memiliki gejala yang jelas seperti suasana hati yang sedih, tertekan, serta kehilangan minat untuk melakukan aktivitas dalam jangka waktu panjang."
         k "Depresi banyak pemicunya mulai dari stres, trauma, rasa tertekan, faktor keturunan, hingga hormon."
         hide sergei
         show sergeibuka
         k "Untuk itu apabila ada orang yang mengalami stres yang berlebihan, alangkah baiknya untuk berkonsultasi kepada psikolog"
    menu:
        "Apakah mereka bisa sembuh?":
         k "Kuncinya adalah mengatur pola hidup dan mengikuti anjuran serta obat yang diberikan oleh psikaternya sehingga kita bisa menghindari kemungkinan terburuk"
    menu:
        "Kemungkinan terburuk?":
         hide sergei
         show sergeibuka
         k "Apabila gangguan jiwa tidak ditangani dengan tepat, dapat memperburuk keadaan atau bahkan menyebabkan kematian"
         k "Tidak seperti penyakit fisik yang menyebabkan kematian karena menggerogoti tubuh penderitanya."
         k "Pengidap gangguan mental akan tersiksa karena pikirannya dan dapat mengakhiri hidupnya apabila memang dirasa oleh mereka tidak ada pilihan lain"
         hide sergeibuka
         show sergei
         k "Hal itu yang harus kita cegah"
         hide sergei
         show rudikasihan with dissolve
         r "Ternyata cukup berbahaya ya"

    menu:
        "Terimakasih pak atas informasinya":
            hide rudikasihan
            show sergei
            k "Sama-sama, semoga temanmu cepat sembuh"

    scene hitam with fade
    "Keesokan harinya"
    scene kelas with dissolve
    show rudismug with dissolve
    r "Haaa, akhirnya kelas berakhir, hari ini capek banget"
    menu:
        "Iya, melelahkan...":
         hide rudismug
         show rudipenasaran
         r "Kenapa kamu jadi lemes banget, apa karena mikirin Hana?"
        "...":
         hide rudismug
         show rudipenasaran
         r "Kenapa? Masih kepikiran Hana?"
    y "Ehh, ngomong-ngomong, Hana dimana, kok kayaknya dia gak kelihatan setelah istirahat tadi?"
    r "Iya ya, ayo coba kita cek ke lapangan"
    scene its with dissolve
    show crimmi
    show bulli1
    show bulli2
    with dissolve
    " "
    r "Eh, itu Hana lagi dibully loh, bantuin nggak?"
    menu:
        "Bantu Hana":
            jump good1
        "Tinggalkan Hana":
            jump bad1


    label good1:
    y "Hana, kamu dicariin pak Dosen tuh, ayo ikut aku"
    hide crimmi
    show crimmibuka
    h "Ah, i- iya"
    scene kelas
    show crimmi
    with pushright
    h "Mana pak Dosen?"
    menu:
        "Aku dosennya":
            h "Jangan bercanda"
        "Sebenarnya tidak ada dosen":
            h "Jadi untuk apa kamu panggil aku"
    r "Kami manggil kamu untuk berbicara"
    if emosi >= 3 :
        jump endingbad1

    if emosi < 3:
        jump endinggood1



    label bad1:
        y "Lebih baik kita kembali ke kelas"
        scene kelas with moveinright
        y "Haah memang lebih enak untuk tidur di kelas"
        show rudikecewa with dis
        r "?"
        hide rudikecewa with dissolve
        show rudipenasaran with dissolve
        r "Eh, coba kamu lihat ini"
        "Hari ini langit terlihat sama murungnya denganku, mungkin kepergianku akan membuat langit menjadi cerah"

        y "Apa ini, ini tulisan Hana kan? Apa Hana mencoba untuk bunuh diri?"
        hide rudipenasaran
        show rudikaget
        r "Hah, bunuh diri??"
        y "Aku harus segera mencari Hana, perasaanku tidak enak"

        scene rooftop
        y "HANAAAA"
        show crimmi with dis
        h "[y]?"
        y "Hana, apa yang kamu lakukan, jangan melompat, dengarkan aku dulu"
        menu:
             "Mengakhiri hidupmu bukan cara untuk menyelesaikan masalahmu":
              jump goodending2
             "Kamu bodoh ya, ngapain kamu loncat nyari sensasi saja":
              jump badending2

label badending2:
    scene rudimarah2
    show rudikaget
    r "Wow"
    hide rudikaget
    show rudipenasaran
    r "Ini serius nih"
    r "Kamu bakalan pilih yang itu?"
    hide rudipenasaran
    show rudikaget
    r "..."
    r "Aku tidak bertanggungjawab karena kamu yang mengontrol pilihan kamu di game ini"
    r "Tapi apakah kamu yakin?"
    menu:
        "iya":
            r "Benar-benar mengejutkan, baiklah"
            jump endingbad2
        "tidak":
            r "Akhirnya kamu paham"
            scene rooftop
            show crimmi
            menu:
             "Mengakhiri hidupmu bukan cara untuk menyelesaikan masalahmu":
                 jump goodending2


label endingbad2:
    scene rooftop
    show crimmi
    h "Memang benar kok, aku hanya mencari perhatian"
    hide crimmi
    show crimminangis
    h "Keberadaanku disini memang hanya menjadi beban saja"
    hide crimminangis
    show crimmiterisak
    h "Makanya aku lebih baik tidak ada disini daripada menjadi beban"
    hide crimmiterisak
    show crimminangis
    h "Selamat tinggal [y]"
    hide crimminangis with dissolve
    pause
    "Kamu menyaksikan Hana loncat dari atap"
    show rudikecewa
    r ". . ."
    jump ending1


label goodending2:
scene rooftop
show crimmi
h "Memangnya kamu tahu apa dari yang kurasakan? Aku benar-benar sudah tidak tahan lagi, kumohon jangan hentikan aku"
y "Aku memang tidak tahu apa yang kamu rasakan, tapi aku paham kalau kamu sedang sakit, mereka salah Hana, kamu bukan orang gila"
y "Kamu bisa kok cerita samaku jika butuh teman bicara, kamu bisa bagikan padaku apa yang kamu rasakan agar kamu lebih terasa ringan, jangan melaluinya sendiri Hana, itu hanya mempersulitmu"
hide crimmi
show rudikaget
r "Iya kok, kamu masih bisa cerita dengan kami"
hide rudikaget
show crimminangis
y "Ayo Hana, gaperlu sampai begitu, ikut aku yuk"
h "Baiklah"
"Kamu berhasil meraih hana"
h "Selama ini aku selalu memiliki pikiran untuk mengakhiri hidupku sendiri, betapa mengerikannya aku, tapi aku terlalu takut untuk melakukannya"
hide crimminangis
show crimminangisgembira
h "Aku sebenarnya masih ingin hidup, [y]"
y "Kamu bisa kok, memilih untuk sembuh dan hidup lebih baik"
hide crimmi


scene its with fade
pause
show crimminormal with dissolve
h "[y], apa kamu sedang santai?"
y "Iya, Hana aku lagi santai kok hehe"
hide crimminormal
show crimminormalbuka
h "Sebelumnya, aku mau bilang terima kasih sama kamu karena sudah menyadarkan aku waktu itu, aku benar-benar berterimakasih. Maukah kamu meluangkan waktu sebentar untuk mendengar ceritaku?"
y "Iya tentu saja, akan aku dengarkan"
h "Kamu tahu kan selama ini aku selalu mempertaruhkan segalanya dengan belajar keras saja, tapi semester lalu tiba-tiba aku merasa sangat kehilangan motivasi belajarku."
h "Sedikit demi sedikit aku menyadari aku tidak tahu apa yang mau aku lakukan di masa depan nanti, aku tidak punya tujuan yang jelas."
hide crimminormalbuka
show crimminormal
h "Aku berpikir bahwa cukup dengan banyak belajar maka hidupku akan jadi lebih baik, ternyata hal itu lebih rumit. Aku merasa tertekan dengan masa depan yang tidak pasti dan sangat mengkhawatirkannya."
h "Terlebih lagi, orang-orang di sekitarku, terutama orang tuaku sendiri menaruh harapan besar padaku karena aku adalah anak pertama."
h "Kemudian, saat aku dipaksa untuk bertemu psikiater oleh orang tuaku, aku didiagnosis mengalami depresi, yang kemungkinan ada karena perasaan-perasaan negatif yang aku rasakan."
h "Aku merasa sangat takut disebut sebagai orang gila dan dipandang buruk oleh orang-orang karena penyakitku ini, makanya aku tidak lanjut untuk berobat. Menurutmu apa yang harus aku lakukan?"
menu:
    "Tenang Hana, kamu hanya perlu memotivasi dirimu":
        y "Lakukan apa yang psikiatermu sampaikan, dan sekali lagi, mengalami depresi bukan berarti kamu adalah orang gila."
        y "Mereka salah Hana, kamu bisa percaya padaku dan orang-orang lain yang juga mendukungmu"
        h "..."
        y "Kalau kamu mau kita bisa coba konsul ke psikolog sekolah, tidak perlu takut"
        hide crimminormal
        show crimminormalbuka
        h "Beneran?"
        y "Iya dong, kita kan teman"
        hide crimminormalbuka
        show rudi
        r "Lagipula kami baru disitu kemarin"
        hide rudi
        show crimmisenyum
        h "Baiklah, aku ingin sembuh sepenuhnya karena aku harus menyayangi hidupku"
        menu:
            "Gitu dong, ini baru semangat Hana yang aku kenal, Hahahaha":
                h "hehehe"
            "Nah, kalau begini kan bagus":
                h "hehehe"
        y "Wah, akhirnya kamu mulai senyum juga"
        h "Terima kasih ya [y] karena telah mendengarkan ceritaku"
        y "Bukan masalah, bagiku siapapun butuh setidaknya satu orang untuk mendengarkan ceritanya, mungkin tidak akan menyelesaikan masalah tapi setidaknya memperingan kondisi karena merasa ada seseorang di pihakmu"
        jump endscreen

label endingbad1:
    h "Mau bicarakan apa?"
    y "Kami khawatir dengan keadaanmu, sepertinya kamu butuh bantuan"
    hide crimmi
    show crimmibuka
    h "Bantuan?"
    hide crimmibuka
    show crimmikecewa
    h "Setelah tindakan kamu selama ini kamu malah menawarkan bantuan?"
    hide crimmikecewa
    show crimmi
    h "Nggak"
    h "Terimakasih"
    hide crimmi
    show crimmimarah
    h "Ternyata aku memang dikelilingi orang munafik yang selalu ingin mencari kesempatan"
    y "Tapi Hana, bukan itu maksud-"
    hide crimmimarah
    show crimmimarah with hpunch
    h "Cukup"
    h "Aku tidak ingin melihat wajah kalian lagi"
    hide crimmimarah
    show crimmi
    h "Selamat tinggal"
    hide crimmi with moveoutleft
    pause
    show rudikecewa with dis
    r "..."
    r "Lebih baik kita pulang saja"
    scene hitam with dissolve
    "Keesokan harinya"
    scene its
    show rudipenasaran with dis
    r "..."
    r "Hana tidak datang ya?"
    y "Sepertinya begitu"
    scene hitam with dissolve
    "Satu bulan kemudian"
    scene its
    show rudikecewa with dissolve
    r "..."
    r "Sepertinya dia tidak akan masuk kampus lagi"
    r "Aku juga mengunjungi rumahnya tapi lampunya mati"
    r "Kita melakukan kesalahan"
    jump ending1

label endinggood1:
    h "Mau berbicara soal apa"
    hide crimmi
    show rudisenyum with dis
    r "Kami sebenarnya khawatir dengan situasimu Hana"
    y "Maukah kamu bercerita lebih banyak tentang situasimu?"
    hide rudisenyum
    show crimmi with dis
    h "..."
    h "Sebenarnya, aku sudah tidak tahan lagi"
    h "Aku selalu dipaksa oleh orangtuaku untuk mendapatkan nilai yang sangat tinggi. Aku dipaksa untuk menjadi apa yang mereka inginkan."
    hide crimmi
    show crimmibuka
    h "Aku terus menerus belajar, tapi aku sendiri tidak tahu dimana potensiku"
    h "Seharusnya semua berjalan dengan lancar dan aku dapat lulus dengan tenang"
    hide crimmibuka
    show crimmi
    h "Tapi tiba-tiba, nafsu makanku menurun, berat badanku berkurang, dan aku jadi sulit tidur."
    h "Nilaiku ikut menurun, dan akhirnya akupun dibully"
    hide crimmi
    show crimminangis
    h "Orang tuaku sangat kesal melihat perbuatanku, dan menyuruhku ke psikiater. Aku harus mengikuti saran mereka, dan akhirnya aku didiagnosis gila."
    h "Aku sudah tidak memiliki niat hidup lagi"
    menu:
        "Diagnosis itu bukan berarti kamu gila":
            h "Apa maksudmu?"
            y "Diagnosis itu hanya menunjukkan kondisi mentalmu saat ini tidak ada hubungannya dengan kegilaan"
            y "Kamu juga telah diberi saran olehnya untuk memperbaiki kondisimu"
            y "Kalau kamu masih merasa bingung, kamu bisa tanya ke psikolog di kampus kita"
            h "Tapi aku takut, aku akan dicap gila lagi apabila datang kesana"
            y "Jangan takut, aku akan ikut denganmu kok"
            hide crimminangis
            show crimmi
            h "Beneran?"
            y "Iya dong, itulah gunanya teman, Rudi juga bakalan ikut kalau kamu mau"
            hide crimmi
            show rudisenyum with dis
            r "Wah, kok aku jadi dibawa-bawa, hahaha. Tapi kalau memang aku harus ikut juga gapapa"
            y "Yaudah yuk, kita sama-sama bantu Hana supaya sembuh, Hana juga pasti mau sembuh kan?"
            hide rudisenyum
            show crimmi with dissolve
            h "Iya, aku mau sembuh"
            y "Nah, gitu dong, ini baru Hana yang kami kenal"
            jump endscreen






label ending1:
    stop music fadeout 0.5
    scene hitam with fade
    "Game Over"
    show rudikecewa with dis
    r "Sudah kuduga akan seperti ini"
    hide rudikecewa
    show rudismug with pixellate
    r "Aku sudah memperingatkanmu berkali-kali"
    hide rudismug
    show rudisenyum
    r "Yah, beginilah akhirnya"
    hide rudisenyum
    show rudingamok
    r "Jadi ?"
    "Restart?"
    menu:
        "Ya":
            r "Berusahalah lebih keras"
            hide rudingamok with fade
            jump start
        "Tidak":
            hide rudingamok
            show rudikecewa
            r "Setidaknya coba lagi untuk lebih baik"
            jump endscreen1



label endscreen:
    stop music fadeout 0.5
    scene hitam with dissolve
    "The End"
    "Seorang teman sejati adalah dia yang berpikir bahwa anda telur yang baik meskipun dia tahu bahwa anda memiliki retak.
     - Bernard Meltzer"

label endscreen1:
    stop music fadeout 0.5
    "The End"

return
