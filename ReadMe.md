# İş Başvurusu E-posta Gönderici

Bu Python betiği, SMTP protokolünü kullanarak iş başvurusu e-postalarını otomatik olarak göndermek için tasarlanmıştır.

## Kullanım

1. Öncelikle, Gmail hesabınızın güvenlik ayarlarından "İki Aşamalı Doğrulama" özelliğini etkinleştirmeniz gerekmektedir. Google, 30 Mayıs 2022'den sonra doğrudan şifrenizi kullanarak uygulama oturumu açmanıza izin vermemektedir. Bu nedenle, hesabınızda "İki Aşamalı Doğrulama" etkinleştirin ve "Uygulama Şifreleri" bölümünden ilgili adımları izleyerek 16 haneli tek kullanımlık bir şifre oluşturun. Bu şifreyi 'password' değişkenine girerek kodunuzun başarılı bir şekilde çalışmasını sağlayabilirsiniz.

2. Betiği çalıştırmadan önce, 'sender_email' ve 'password' değişkenlerine Gmail hesap bilgilerinizi, 'filename' değişkenine göndermek istediğiniz CV dosyasının adını ve 'recipient_email' değişkenine alıcı e-posta adresini giriniz.

3. Betiği çalıştırdığınızda, e-posta adresi girişi istenecektir. Geçerli bir e-posta adresi giriniz.

4. E-posta gönderme tarihini ve saatinde belirtmek isterseniz, isteğe bağlı olarak YYYY-MM-DD HH:MM formatında bir tarih ve saat giriniz. Belirtilen tarih ve saatte e-posta otomatik olarak gönderilecektir.

5. Betiği çalıştırdığınızda, iş başvurusu e-postası gönderilecek ve sonuç ekrana yazdırılacaktır.

## Notlar

- Bu kod, yalnızca Gmail üzerinden e-posta göndermek için tasarlanmıştır.
- E-posta içeriğini ve gönderim tarihini/saatini isteğinize göre düzenleyebilirsiniz.

# Job Application Email Sender

This Python script is designed to automatically send job application emails using the SMTP protocol.

## Usage

1. Firstly, you need to enable "Two-Factor Authentication" for your Gmail account in its security settings. Google no longer allows you to sign in to apps directly using your password as of May 30, 2022. Therefore, enable "Two-Factor Authentication" for your account and generate a 16-digit one-time password from the "App Passwords" section. You can enter this password into the `password` variable to ensure your code runs successfully.

2. Before running the script, input your Gmail account details into the `sender_email` and `password` variables, the name of the CV file you want to send into the `filename` variable, and the recipient email address into the `recipient_email` variable.

3. When you run the script, you will be prompted to enter an email address. Enter a valid email address.

4. Optionally, if you want to specify the date and time to send the email, enter a date and time in the format `YYYY-MM-DD HH:MM`. The email will be automatically sent at the specified date and time.

5. When you run the script, the job application email will be sent, and the result will be printed to the screen.

## Notes

- This code is designed to send emails only through Gmail.
- You can customize the email content and specify the sending date/time as per your preference.
