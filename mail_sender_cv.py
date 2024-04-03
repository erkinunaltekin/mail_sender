import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re
from datetime import datetime

def get_valid_email():
    while True:
        email = input("Gönderilecek mail adresini giriniz: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Geçersiz e-posta adresi. Lütfen geçerli bir e-posta adresi girin.")

def send_email(sender_email, password, recipient_email, application_message, filename, scheduled_time=None):
    # MIME Multipart nesnesi oluşturma
    message = MIMEMultipart()
    message['Subject'] = 'İş Başvurusu'
    message['From'] = sender_email
    message['To'] = recipient_email

    # Metin mesajını ekleyin
    application_message = application_message.format(recipient_name=recipient_email.split('@')[0])
    message.attach(MIMEText(application_message, 'plain'))

    # Ek dosya ekleme
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= {filename}',
    )
    message.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            if scheduled_time:
                scheduled_time = datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M")
                now = datetime.now()
                if scheduled_time > now:
                    delay = (scheduled_time - now).total_seconds()
                    print(f"Mail {scheduled_time} tarihinde saat {scheduled_time.strftime('%H:%M')} 'de gönderilecek.")
                    server.sendmail(sender_email, recipient_email, message.as_string())
                    print("İş başvurunuz başarıyla planlandı.")
                else:
                    print("Geçmiş bir tarih veya saat seçtiniz. Mail hemen gönderilecek.")
                    server.sendmail(sender_email, recipient_email, message.as_string())
                    print("İş başvurunuz başarıyla gönderildi.")
            else:
                server.sendmail(sender_email, recipient_email, message.as_string())
                print("İş başvurunuz başarıyla gönderildi.")
    except smtplib.SMTPAuthenticationError:
        print('Hata: Kimlik doğrulama başarısız oldu.')
    except smtplib.SMTPException as e:
        print(f'Hata: E-posta gönderilemedi. {e}')

if __name__ == "__main__":
    sender_email = 'Your_Email@gmail.com' #EMAİL ADRESİNİZİ GİRİNİZ
    password = 'Your_Password' #GOOGLE HESABINIZIN AYARLARINDAN UYGULAMA ŞİFRELERİ MENÜSÜNDEN ŞİFRE ALINIZ VE O ŞİFREYİ GİRİNİZ
    recipient_email = get_valid_email()
    application_message = """
    Merhaba Sayın Yetkili,

    İş başvurumu iletmek için bu e-postayı yazıyorum. İlgili pozisyon için kendime uygun olduğuna inanıyorum ve ekteki özgeçmişimle detayları bulabilirsiniz.

    Size daha fazla bilgi verebilmem için sabırsızlanıyorum. Eğer uygun görürseniz, bir görüşme yapmak için hazırım.

    Saygılarımla,
    [Adınız]
    """
    filename = 'cv.pdf'  # Eklemek istediğiniz dosyanın adını buraya yazın dosya programın yüklü olduğu yerde olmalıdır.
    scheduled_time = input("Gönderim tarihini ve saatini (YYYY-MM-DD HH:MM formatında) belirtmek isterseniz yazın (isteğe bağlı): ")
    send_email(sender_email, password, recipient_email, application_message, filename, scheduled_time)
