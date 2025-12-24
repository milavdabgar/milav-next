---
title: "WordPress સાઇટને HTTP થી HTTPS પર કેવી રીતે મૂવ કરવી: એક સંપૂર્ણ ગાઇડ"
date: "2025-03-05"
description: "તમારી WordPress સાઇટને HTTP થી HTTPS પર Let's Encrypt સર્ટિફિકેટનો ઉપયોગ કરીને મૂવ કરવા માટેની સ્ટેપ-બાય-સ્ટેપ ગાઇડ"
summary: "આ કોમ્પ્રિહેન્સિવ ટ્યુટોરિયલ તમને તમારી WordPress સાઇટને HTTP થી HTTPS પર Let's Encrypt SSL સર્ટિફિકેટ્સનો ઉપયોગ કરીને મૂવ કરવાની પ્રક્રિયા શીખવાડે છે. તમે સર્ટિફિકેટ્સ કેવી રીતે મેળવવા, Apache કોન્ફિગર કરવા, WordPress સેટિંગ્સ અપડેટ કરવા અને તમારી સાઇટને માઇગ્રેશન પછી પરફેક્ટ રીતે કામ કરતી બનાવવા વિશે શીખશો."
tags: ["wordpress", "ssl", "https", "security", "letsencrypt", "certbot", "cloudflare", "apache"]
---

## પરિચય

આધુનિક વેબસાઇટ્સ માટે HTTPS હવે એક વિકલ્પ નથી, પણ જરૂરિયાત છે. સર્ચ એન્જિન સિક્યોર સાઇટ્સને પ્રાધાન્ય આપે છે, બ્રાઉઝર્સ નોન-સિક્યોર સાઇટ્સ માટે વોર્નિંગ મેસેજ દર્શાવે છે, અને વિઝિટર્સ HTTPS દ્વારા મળતી સિક્યુરિટીની અપેક્ષા રાખે છે. આ ગાઇડ તમને તમારી WordPress સાઇટને HTTP થી HTTPS પર મૂવ કરવાની સંપૂર્ણ પ્રોસેસ શીખવાડશે, જેમાં અમે ફ્રી Let's Encrypt SSL સર્ટિફિકેટ્સનો ઉપયોગ કરીશું.

**પૂર્વ જરૂરિયાતો:**

- LAMP સર્વર (Linux, Apache, MySQL, PHP) પર ચાલતી WordPress સાઇટ
- તમારા સર્વર પર SSH એક્સેસ
- કમાન્ડ લાઇનનું બેઝિક જ્ઞાન
- Cloudflare દ્વારા મેનેજ થતા DNS સાથેનું ડોમેન (વાઇલ્ડકાર્ડ સર્ટિફિકેટ્સ માટે)

જો તમે હજુ સુધી LAMP સર્વર પર WordPress સેટઅપ કર્યું નથી, તો પહેલા અમારી [Raspberry Pi WordPress સેટઅપ ગાઇડ](https://planetmilav.com/raspberrypisetup/) ફોલો કરો.

## સ્ટેપ 1: Certbot ઇન્સ્ટોલ કરો

Certbot એ Let's Encrypt નો ઓફિશિયલ ક્લાયન્ટ છે જે SSL સર્ટિફિકેટ્સ મેળવવાની અને રિન્યૂ કરવાની પ્રક્રિયાને સરળ બનાવે છે. નીચેના કમાન્ડનો ઉપયોગ કરીને Certbot અને Apache પ્લગિન ઇન્સ્ટોલ કરો:

```bash
sudo apt update
sudo apt install certbot python3-certbot-apache
```

> **નોંધ:** ઓરિજિનલ પોસ્ટમાં `python-certbot-apache -t stretch-backports` ઉપયોગ થયો હતો જે હવે જૂનો થઈ ગયો છે. આધુનિક Debian/Ubuntu ડિસ્ટ્રિબ્યુશન્સ બેકપોર્ટ્સની જરૂર વિના Python 3 વર્ઝનનો ઉપયોગ કરે છે.

## સ્ટેપ 2: તમારા સર્ટિફિકેટનો પ્રકાર પસંદ કરો

તમારી પાસે SSL સર્ટિફિકેટ્સ માટે બે વિકલ્પો છે:

### વિકલ્પ A: સિંગલ ડોમેન સર્ટિફિકેટ

જો તમારે માત્ર એક જ ડોમેન સિક્યોર કરવાની જરૂર હોય, તો ચલાવો:

```bash
sudo certbot --apache
```

આ તમને એક ઇન્ટરેક્ટિવ પ્રોસેસ દ્વારા લઈ જશે જેમાં તમે કયા ડોમેન સિક્યોર કરવા તે પસંદ કરી શકશો અને ઓટોમેટિકલી તમારા માટે Apache કોન્ફિગર કરશે.

વધુ કંટ્રોલ માટે, તમે આનો ઉપયોગ કરી શકો છો:

```bash
sudo certbot certonly --apache
```

આ તમારા Apache કોન્ફિગરેશનમાં ફેરફાર કર્યા વિના સર્ટિફિકેટ મેળવે છે, જેથી તમને સેટઅપ પર વધુ કંટ્રોલ મળે છે.

### વિકલ્પ B: Cloudflare DNS સાથે વાઇલ્ડકાર્ડ સર્ટિફિકેટ (રિકમેન્ડેડ)

વાઇલ્ડકાર્ડ સર્ટિફિકેટ તમારા મુખ્ય ડોમેન અને બધા સબડોમેન (દા.ત., `example.com` અને `*.example.com`) ને કવર કરે છે. જો તમે મલ્ટિપલ સબડોમેન ચલાવતા હો, તો આ આદર્શ છે.

1. Certbot માટે Cloudflare DNS પ્લગિન ઇન્સ્ટોલ કરો:

```bash
sudo pip3 install certbot-dns-cloudflare
```

2. Cloudflare API કોન્ફિગરેશન ફાઇલ બનાવો:

```bash
sudo mkdir -p /etc/letsencrypt/
sudo nano /etc/letsencrypt/cloudflare.ini
```

3. તમારા Cloudflare એકાઉન્ટની વિગતો ઉમેરો:

```ini
dns_cloudflare_email = 'your-cloudflare-email@example.com'
dns_cloudflare_api_key = 'your-global-api-key'
```

> **સિક્યુરિટી નોંધ:** તમારી Global API key મેળવવા માટે, Cloudflare માં લોગિન કરો, તમારી પ્રોફાઇલ પર જાઓ, અને API Tokens સેક્શન જુઓ. વધુ સારી સિક્યુરિટી માટે, ગ્લોબલ કી ને બદલે સ્કોપ્ડ API ટોકન્સનો ઉપયોગ કરવા વિચારો.

4. અનધિકૃત એક્સેસને રોકવા માટે કોન્ફિગરેશન ફાઇલને સિક્યોર કરો:

```bash
sudo chmod 600 /etc/letsencrypt/cloudflare.ini
```

5. વાઇલ્ડકાર્ડ સર્ટિફિકેટ મેળવો:

```bash
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials /etc/letsencrypt/cloudflare.ini -d yourdomain.com,*.yourdomain.com --preferred-challenges dns-01
```

`yourdomain.com` ને તમારા વાસ્તવિક ડોમેન નામથી બદલો.

## સ્ટેપ 3: HTTPS માટે Apache કોન્ફિગર કરો

### ડિફોલ્ટ SSL સાઇટ કોન્ફિગર કરો

જો તમારી WordPress સાઇટ ડિફોલ્ટ `/var/www/html` ડિરેક્ટરીમાં છે, તો ડિફોલ્ટ SSL કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /etc/apache2/sites-available/default-ssl.conf
```

ફાઇલને નીચેની સામગ્રી સાથે અપડેટ કરો (તમારા ડોમેન સાથે `yourdomain.com` ને બદલો):

```apache
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerAdmin webmaster@localhost
        ServerName yourdomain.com
        ServerAlias www.yourdomain.com

        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        SSLEngine on
        SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem
        Include /etc/letsencrypt/options-ssl-apache.conf

        <Directory /var/www/html>
            Options FollowSymLinks
            AllowOverride All
            Require all granted
        </Directory>
    </VirtualHost>
</IfModule>
```

જો તમારી સાઇટ કસ્ટમ ડિરેક્ટરીમાં છે, તો `DocumentRoot` અને `<Directory>` પાથને અનુકૂળ બનાવો.

### SSL મોડ્યુલ્સ અને કોન્ફિગરેશન એનેબલ કરો

```bash
sudo a2enmod ssl
sudo a2enmod headers
sudo a2ensite default-ssl.conf
sudo systemctl restart apache2
```

### HTTP થી HTTPS રીડાયરેક્શન કોન્ફિગર કરો (રિકમેન્ડેડ)

તમારા HTTP VirtualHost કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

`<VirtualHost *:80>` બ્લોકમાં નીચેના રીડાયરેક્શન રૂલ્સ ઉમેરો:

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    
    # અન્ય કોન્ફિગરેશન...
    
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>
```

રિરાઇટ મોડ્યુલ એનેબલ કરો અને Apache રીસ્ટાર્ટ કરો:

```bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

## સ્ટેપ 4: WordPress સેટિંગ્સ અપડેટ કરો

### WordPress એડમિનમાં સાઇટ URL અપડેટ કરો

1. તમારા WordPress એડમિન ડેશબોર્ડમાં લોગિન કરો
2. Settings → General પર જાઓ
3. "WordPress Address (URL)" અને "Site Address (URL)" બંનેને `http://` ની જગ્યાએ `https://` વાપરવા માટે અપડેટ કરો
4. ચેન્જિસ સેવ કરો

જો આ સેટિંગ્સ બદલ્યા પછી સમસ્યાઓ (જેમ કે વ્હાઇટ સ્ક્રીન અથવા લોગિન સમસ્યાઓ) આવે, તો તમે MySQL નો ઉપયોગ કરીને તેમને ફિક્સ કરી શકો છો:

```bash
mysql -u root -p
use wordpress;   # જો અલગ હોય તો તમારા અસલ ડેટાબેસ નામથી બદલો
update wp_options set option_value = 'https://yourdomain.com' where option_name = 'siteurl';
update wp_options set option_value = 'https://yourdomain.com' where option_name = 'home';
exit;
```

### wp-config.php મોડિફાય કરો

નીચેનો કોડ તમારી `wp-config.php` ફાઇલમાં ઉમેરો, જે લાઇન કહે છે `require_once(ABSPATH . 'wp-settings.php');` તેની પહેલાં:

```php
/* SSL સેટિંગ્સ */
define('FORCE_SSL_ADMIN', true);

/* યોગ્ય WordPress ડિટેક્શન માટે HTTPS 'on' કરો */
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
    $_SERVER['HTTPS'] = 'on';
}
```

આ WordPress ને યોગ્ય રીતે HTTPS ડિટેક્ટ કરવામાં મદદ કરે છે, ખાસ કરીને પ્રોક્સી અથવા લોડ બેલેન્સર પાછળ હોય ત્યારે.

## સ્ટેપ 5: તમારા ડેટાબેસમાં ઇન્ટરનલ લિંક્સ અપડેટ કરો

ડેટાબેસમાં પોસ્ટ્સ, પેજીસ અને ઓપ્શન્સમાં HTTP લિંક્સ હાર્ડકોડેડ હોઈ શકે છે. આને ફિક્સ કરવા માટે "Better Search Replace" પ્લગિનનો ઉપયોગ કરો:

1. "Better Search Replace" પ્લગિન ઇન્સ્ટોલ કરો (તે જૂના "Search and Replace" પ્લગિન કરતા વધુ સુરક્ષિત અને ફીચર-રિચ છે)
2. Tools → Better Search Replace પર જાઓ
3. "Search for" ફીલ્ડમાં, `http://yourdomain.com` દાખલ કરો
4. "Replace with" ફીલ્ડમાં, `https://yourdomain.com` દાખલ કરો
5. transients વાળા ટેબલ સિવાય બધા ટેબલ્સ સિલેક્ટ કરો
6. પહેલા "Run as dry run" ઓપ્શન એનેબલ કરો જેથી શું બદલાશે તે જોઈ શકાય
7. જો રિઝલ્ટ્સ સારા લાગે, તો "Run as dry run" અનચેક કરો અને સર્ચ/રિપ્લેસ વાસ્તવમાં ચલાવો

## સ્ટેપ 6: ઓટોમેટિક સર્ટિફિકેટ રિન્યૂઅલ સેટ કરો

Let's Encrypt સર્ટિફિકેટ્સ 90 દિવસ પછી એક્સપાયર થાય છે, તેથી ઓટોમેટિક રિન્યૂઅલ સેટ કરવું ખૂબ જરૂરી છે:

```bash
sudo crontab -e
```

રિન્યૂઅલ ચેક દરરોજ બે વખત (Let's Encrypt દ્વારા ભલામણ કરેલ) ચલાવવા માટે નીચેની લાઇન ઉમેરો:

```bash
0 3,15 * * * certbot renew --quiet --post-hook "systemctl reload apache2" > /dev/null 2>&1
```

## સ્ટેપ 7: તમારા HTTPS સેટઅપની ટેસ્ટ કરો

તમારા SSL કોન્ફિગરેશનની ચકાસણી માટે આ ટૂલ્સની મુલાકાત લો:

1. [SSL Labs Server Test](https://www.ssllabs.com/ssltest/)
2. [Why No Padlock](https://www.whynopadlock.com/)

આ બાબતો ચેક કરો:

- માન્ય સર્ટિફિકેટ
- કોઈ મિક્સ્ડ કન્ટેન્ટ વોર્નિંગ નથી
- યોગ્ય રીડાયરેક્ટ્સ

## ટ્રબલશૂટિંગ

### મિક્સ્ડ કન્ટેન્ટ વોર્નિંગ્સ

જો તમારા બ્રાઉઝરના કન્સોલમાં મિક્સ્ડ કન્ટેન્ટ વોર્નિંગ્સ દેખાય છે:

1. કોઈપણ બાકી રહેલા `http://` રેફરન્સીસ શોધવા માટે "Better Search Replace" પ્લગિનનો ફરીથી ઉપયોગ કરો
2. હાર્ડકોડેડ HTTP URLs માટે તમારા થીમ અને પ્લગિન ફાઇલ્સ ચેક કરો
3. મિક્સ્ડ કન્ટેન્ટ ઇશ્યુને ઓટોમેટિકલી ફિક્સ કરવા માટે "Really Simple SSL" પ્લગિનનો ઉપયોગ કરવાનું વિચારો

### URL ચેન્જ પછી વ્હાઇટ સ્ક્રીન

જો તમને વ્હાઇટ સ્ક્રીન મળે:

1. સીધા HTTPS સાથે wp-admin એક્સેસ કરવાનો પ્રયાસ કરો
2. ઉપર જણાવેલા MySQL ફિક્સનો ઉપયોગ કરો
3. ફાઇલ પરમિશન્સ અને ઓનરશિપની ચકાસણી કરો

### સર્ટિફિકેટ રિન્યૂઅલ ઇશ્યુઝ

જો ઓટોમેટિક રિન્યૂઅલ નિષ્ફળ જાય:

1. રિન્યૂઅલ પ્રોસેસને મેન્યુઅલી ટેસ્ટ કરો: `sudo certbot renew --dry-run`
2. લોગ્સ ચેક કરો: `sudo journalctl -xe`
3. ખાતરી કરો કે Cloudflare API ક્રેડન્શિયલ્સ સાચા છે (વાઇલ્ડકાર્ડ સર્ટિફિકેટ્સ માટે)

## ઉપસંહાર

અભિનંદન! તમારી WordPress સાઇટ હવે HTTPS સાથે પૂર્ણપણે સિક્યોર છે. આ તમારી સાઇટની સિક્યુરિટી, SEO રેન્કિંગ અને યુઝર ટ્રસ્ટ સુધારે છે. યાદ રાખો:

- સર્ટિફિકેટ એક્સપાયરેશન પર નજર રાખો (જોકે ઓટોમેટિક રિન્યૂઅલ આને સંભાળી લેવું જોઈએ)
- નવી સામગ્રી ઉમેરતી વખતે મિક્સ્ડ કન્ટેન્ટ વોર્નિંગ્સ પર ધ્યાન રાખો
- HTTP Strict Transport Security (HSTS) જેવા વધારાના સિક્યુરિટી પગલાંઓનો વિચાર કરો

SSL યોગ્ય રીતે કોન્ફિગર થયા પછી, તમારી WordPress સાઇટ હવે વધુ સુરક્ષિત છે અને આધુનિક વેબ માટે તૈયાર છે!

## વધારાના રિસોર્સીસ

- [Let's Encrypt ડોક્યુમેન્ટેશન](https://letsencrypt.org/docs/)
- [Certbot ઇન્સ્ટ્રક્શન્સ](https://certbot.eff.org/)
- [WordPress HTTPS માઇગ્રેશન ગાઇડ](https://www.wpbeginner.com/wp-tutorials/how-to-add-ssl-and-https-in-wordpress/)
- [Cloudflare SSL ડોક્યુમેન્ટેશન](https://developers.cloudflare.com/ssl/)
