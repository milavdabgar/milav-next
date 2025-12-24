---
title: "સંપૂર્ણ ગાઇડ: રાસ્પબેરી પાઈ પર નેક્સ્ટક્લાઉડ સેટઅપ કરવું"
date: 2023-03-05
description: "રાસ્પબેરી પાઈ પર નેક્સ્ટક્લાઉડનો ઉપયોગ કરીને તમારું પોતાનું પ્રાઇવેટ ક્લાઉડ સ્ટોરેજ સોલ્યુશન બનાવવા માટેની વિસ્તૃત ટ્યુટોરિયલ"
summary: "શીખો કેવી રીતે તમારા રાસ્પબેરી પાઈને ઓટોમેટિક બેકઅપ, ફાઇલ સિંકિંગ, મીડિયા સ્ટ્રીમિંગ અને વધુ સાથે શક્તિશાળી પ્રાઇવેટ ક્લાઉડ સર્વરમાં પરિવર્તિત કરવું."
tags: ["raspberry pi", "nextcloud", "self-hosted", "cloud storage", "server", "privacy", "linux", "tutorial"]
---

તમારા રાસ્પબેરી પાઈને નેક્સ્ટક્લાઉડ સાથે શક્તિશાળી, સંપૂર્ણ-ફીચર્ડ પ્રાઇવેટ ક્લાઉડ સ્ટોરેજ સોલ્યુશનમાં પરિવર્તિત કરો. આ વિસ્તૃત ગાઇડ તમને પ્રક્રિયાના દરેક પગલામાં, પ્રારંભિક ઇન્સ્ટોલેશનથી લઈને એડવાન્સ્ડ ઓપ્ટિમાઇઝેશન ટેકનિક્સ સુધી લઈ જાય છે.

## તમે શું મેળવશો

રાસ્પબેરી પાઈ પર તમારા પોતાના નેક્સ્ટક્લાઉડ સર્વર સાથે, તમારી પાસે હશે:

- તમારા ડેટા પર **સંપૂર્ણ નિયંત્રણ** કોઈ થર્ડ-પાર્ટી એક્સેસ વિના
- **અનલિમિટેડ સ્ટોરેજ** ક્ષમતા (ફક્ત તમારા જોડાયેલા ડ્રાઇવ્સ દ્વારા મર્યાદિત)
- તમારા બધા મોબાઇલ ડિવાઇસથી **ઓટોમેટિક ફોટો અને વિડિયો બેકઅપ**
- તમારા બધા કમ્પ્યુટર અને ડિવાઇસ પર **સીમલેસ ફાઇલ સિંક્રોનાઇઝેશન**
- તમારા સંગીત, વિડિયો, અને ફોટા માટે **મીડિયા સ્ટ્રીમિંગ** ક્ષમતાઓ
- કેલેન્ડર, કોન્ટેક્ટ્સ, નોટ્સ, અને ટાસ્ક્સ સહિત **કોલાબોરેશન ટૂલ્સ**
- નેક્સ્ટક્લાઉડ એપ ઇકોસિસ્ટમ દ્વારા **એક્સપેન્ડેબલ ફંક્શનાલિટી**
- કમર્શિયલ ક્લાઉડ સર્વિસીસની તુલનામાં **એન્હાન્સ્ડ પ્રાઇવસી**

## પૂર્વશરતો

શરૂ કરતા પહેલા, ખાતરી કરો કે તમારી પાસે છે:

- **હાર્ડવેર**:
  - રાસ્પબેરી પાઈ 4 (4GB+ RAM રેકમેન્ડેડ) અથવા રાસ્પબેરી પાઈ 5
  - વિશ્વસનીય માઇક્રોSD કાર્ડ (32GB+ રેકમેન્ડેડ)
  - એક્સટર્નલ સ્ટોરેજ ડિવાઇસ (પરફોર્મન્સ માટે USB SSD રેકમેન્ડેડ)
  - વિશ્વસનીય પાવર સપ્લાય (ઓફિશિયલ 15W USB-C રેકમેન્ડેડ)
  - ઈથરનેટ કનેક્શન (રેકમેન્ડેડ) અથવા સ્ટેબલ WiFi

- **સોફ્ટવેર**:
  - લેટેસ્ટ અપડેટ્સ સાથે રાસ્પબેરી પાઈ OS (64-bit રેકમેન્ડેડ)
  - SSH એક્સેસ અથવા ડાયરેક્ટ એક્સેસ માટે કીબોર્ડ/મોનિટર
  - સ્ટેટિક IP એડ્રેસ કોન્ફિગર કરેલ અથવા ડાયનેમિક DNS સેટ અપ કરેલ

- **સ્કિલ્સ**:
  - બેઝિક કમાન્ડ લાઇન નોલેજ
  - નેટવર્કિંગ કોન્સેપ્ટ્સની મૂળભૂત સમજ

## સ્ટેપ 1: તમારી સિસ્ટમ તૈયાર કરો

### તમારી સિસ્ટમ અપડેટ કરો

હંમેશા ખાતરી કરવા માટે કે બધા પેકેજ અપ ટુ ડેટ છે તે માટે એક ફ્રેશ અપડેટથી શરૂ કરો:

```bash
# પેકેજ રિપોઝિટરીઝ અપડેટ કરો અને બધા પેકેજ અપગ્રેડ કરો
sudo apt update && sudo apt full-upgrade -y

# અનિવાર્ય સિસ્ટમ યુટિલિટીઝ ઇન્સ્ટોલ કરો
sudo apt install -y curl wget unzip git htop
```

### સ્વેપ મેમરી કોન્ફિગર કરો (વૈકલ્પિક પરંતુ રેકમેન્ડેડ)

મર્યાદિત RAM સાથે ખાસ કરીને બેટર પરફોર્મન્સ માટે:

```bash
# વર્તમાન સ્વેપ કોન્ફિગરેશન ચેક કરો
free -h

# સ્વેપ સાઇઝને 2GB સુધી વધારો
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```

`CONF_SWAPSIZE=100` ને `CONF_SWAPSIZE=2048` માં બદલો, પછી:

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

## સ્ટેપ 2: જરૂરી સોફ્ટવેર ઇન્સ્ટોલ કરો

LAMP સ્ટેક (Linux, Apache, MariaDB, PHP) અને વધારાના જરૂરી પેકેજ ઇન્સ્ટોલ કરો:

```bash
# Apache વેબ સર્વર ઇન્સ્ટોલ કરો
sudo apt install -y apache2

# MariaDB ડેટાબેસ સર્વર ઇન્સ્ટોલ કરો
sudo apt install -y mariadb-server

# PHP અને જરૂરી એક્સટેન્શન ઇન્સ્ટોલ કરો
sudo apt install -y libapache2-mod-php php-gd php-json php-mysql php-curl 
sudo apt install -y php-mbstring php-intl php-imagick php-xml php-zip 
sudo apt install -y php-bcmath php-gmp php-apcu
```

## સ્ટેપ 3: ઓપ્ટિમલ પરફોર્મન્સ માટે PHP કોન્ફિગર કરો

નેક્સ્ટક્લાઉડ માટે કસ્ટમ PHP કોન્ફિગરેશન ફાઇલ બનાવો:

```bash
# PHP વર્ઝન નક્કી કરો
PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;")

# કસ્ટમ કોન્ફિગરેશન ફાઇલ બનાવો
sudo nano /etc/php/$PHP_VERSION/apache2/conf.d/99-nextcloud.ini
```

આ ઓપ્ટિમાઇઝ્ડ સેટિંગ્સ ઉમેરો:

```ini
; મેમરી અને અપલોડ સેટિંગ્સ
memory_limit = 512M
upload_max_filesize = 1024M
post_max_size = 1024M
max_execution_time = 300

; તમારો ટાઇમઝોન સેટ કરો
date.timezone = Europe/London  ; તમારા ટાઇમઝોન સાથે બદલો

; બેટર પરફોર્મન્સ માટે OpCache સેટિંગ્સ
opcache.enable = 1
opcache.interned_strings_buffer = 8
opcache.max_accelerated_files = 10000
opcache.memory_consumption = 128
opcache.save_comments = 1
opcache.revalidate_freq = 1
```

ફેરફારો લાગુ કરવા માટે Apache રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart apache2
```

## સ્ટેપ 4: MariaDB ડેટાબેસ કોન્ફિગર કરો

MariaDB ઇન્સ્ટોલેશન સુરક્ષિત કરો:

```bash
sudo mysql_secure_installation
```

જ્યારે પૂછવામાં આવે:
- વર્તમાન રૂટ પાસવર્ડ દાખલ કરો (સંભવિત રીતે કોઈ નહીં, ફક્ત એન્ટર દબાવો)
- રૂટ પાસવર્ડ સેટ કરો: Y અને એક મજબૂત પાસવર્ડ દાખલ કરો
- એનોનિમસ યુઝર્સ દૂર કરો: Y
- રિમોટલી રૂટ લોગિનને ના પાડો: Y
- ટેસ્ટ ડેટાબેસ દૂર કરો: Y
- પ્રિવિલેજ ટેબલ્સ રીલોડ કરો: Y

હવે નેક્સ્ટક્લાઉડ માટે ડેડિકેટેડ ડેટાબેસ બનાવો:

```bash
sudo mysql -u root -p
```

જ્યારે પૂછવામાં આવે, ત્યારે તમે સેટ કરેલા રૂટ પાસવર્ડ દાખલ કરો. પછી આ SQL કમાન્ડ્સ ચલાવો:

```sql
CREATE DATABASE nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'nextclouduser'@'localhost' IDENTIFIED BY 'choose-a-secure-password';
GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextclouduser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## સ્ટેપ 5: નેક્સ્ટક્લાઉડ ડાઉનલોડ અને ઇન્સ્ટોલ કરો

નેક્સ્ટક્લાઉડનું લેટેસ્ટ વર્ઝન ડાઉનલોડ અને એક્સટ્રેક્ટ કરો:

```bash
# લેટેસ્ટ રિલીઝ ડાઉનલોડ કરો
cd /tmp
wget https://download.nextcloud.com/server/releases/latest.tar.bz2

# વેબ ડિરેક્ટરીમાં એક્સટ્રેક્ટ કરો
sudo tar -xjf latest.tar.bz2 -C /var/www/

# યોગ્ય ઓનરશિપ સેટ કરો
sudo chown -R www-data:www-data /var/www/nextcloud/
```

## સ્ટેપ 6: નેક્સ્ટક્લાઉડ માટે Apache કોન્ફિગર કરો

નેક્સ્ટક્લાઉડ માટે ડેડિકેટેડ વર્ચ્યુઅલ હોસ્ટ બનાવો:

```bash
sudo nano /etc/apache2/sites-available/nextcloud.conf
```

આ કોન્ફિગરેશન ઉમેરો:

```apache
<VirtualHost *:80>
    DocumentRoot /var/www/nextcloud/
    ServerName your-pi.local

    <Directory /var/www/nextcloud/>
        Options +FollowSymlinks
        AllowOverride All
        Require all granted
        <IfModule mod_dav.c>
            Dav off
        </IfModule>
        SetEnv HOME /var/www/nextcloud
        SetEnv HTTP_HOME /var/www/nextcloud
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/nextcloud_error.log
    CustomLog ${APACHE_LOG_DIR}/nextcloud_access.log combined
</VirtualHost>
```

`your-pi.local` ને તમારા રાસ્પબેરી પાઈના હોસ્ટનેમ અથવા IP એડ્રેસથી બદલો.

સાઇટ કોન્ફિગરેશન અને જરૂરી Apache મોડ્યુલ્સ સક્ષમ કરો:

```bash
# સાઇટ સક્ષમ કરો
sudo a2ensite nextcloud.conf

# જરૂરી મોડ્યુલ્સ સક્ષમ કરો
sudo a2enmod rewrite headers env dir mime setenvif ssl

# Apache રિસ્ટાર્ટ કરો
sudo systemctl restart apache2
```

### સિક્યુરિટી સ્કેન ફિક્સીસ

નેક્સ્ટક્લાઉડ એડમિન પેનલથી સિક્યુરિટી સ્કેન ચલાવો અને તે ઓળખે તેવા કોઈપણ મુદ્દાઓને ફિક્સ કરો.

## સ્ટેપ 7: એક્સટર્નલ સ્ટોરેજ સેટઅપ કરો

પરફોર્મન્સ સુધારવા અને SD કાર્ડ વેર અટકાવવા માટે નેક્સ્ટક્લાઉડ ડેટા માટે એક્સટર્નલ સ્ટોરેજનો ઉપયોગ કરવાની ખૂબ ભલામણ કરવામાં આવે છે.

### તમારા એક્સટર્નલ ડ્રાઇવને ઓળખો

```bash
lsblk -f
```

તમારા એક્સટર્નલ ડ્રાઇવ માટે જુઓ (દા.ત., `/dev/sda1`).

### માઉન્ટ પોઇન્ટ તૈયાર કરો

```bash
# માઉન્ટ ડિરેક્ટરી બનાવો
sudo mkdir -p /mnt/nextcloud-data
```

### ફાઇલસિસ્ટમ ડ્રાઇવર્સ ઇન્સ્ટોલ કરો (જો જરૂરી હોય)

```bash
# NTFS ડ્રાઇવ્સ માટે
sudo apt install -y ntfs-3g

# exFAT ડ્રાઇવ્સ માટે
sudo apt install -y exfat-fuse exfat-utils
```

### ડ્રાઇવ ફોર્મેટ કરો (વૈકલ્પિક - ચેતવણી: બધા ડેટા ભૂંસી નાખે છે)

જો તમારે ડ્રાઇવને ફોર્મેટ કરવાની જરૂર છે (આ ડ્રાઇવ પરના બધા ડેટા કાઢી નાખશે):

```bash
# ext4 (Linux નેટિવ) ફાઇલસિસ્ટમ માટે
sudo mkfs.ext4 /dev/sdX1  # sdX1 ને તમારા ડ્રાઇવ આઇડેન્ટિફાયર સાથે બદલો
```

### ઓટોમેટિક માઉન્ટિંગ સેટઅપ કરો

તમારા ડ્રાઇવનું UUID મેળવો:

```bash
sudo blkid | grep /dev/sdX1  # sdX1 ને તમારા ડ્રાઇવ સાથે બદલો
```

બૂટ પર ઓટોમેટિક માઉન્ટિંગ કોન્ફિગર કરો:

```bash
sudo nano /etc/fstab
```

તમારા ફાઇલસિસ્ટમ પ્રકાર પર આધારિત આમાંથી એક લાઇન ઉમેરો:

ext4 માટે (Linux માટે રેકમેન્ડેડ):
```
UUID=your-drive-uuid /mnt/nextcloud-data ext4 defaults,noatime 0 0
```

NTFS માટે:
```
UUID=your-drive-uuid /mnt/nextcloud-data ntfs-3g defaults,permissions,uid=www-data,gid=www-data,umask=0027 0 0
```

exFAT માટે:
```
UUID=your-drive-uuid /mnt/nextcloud-data exfat defaults,uid=www-data,gid=www-data,umask=0027 0 0
```

ડ્રાઇવ માઉન્ટ કરો:

```bash
sudo mount -a
```

### પરમિશન સેટ કરો

```bash
sudo chown -R www-data:www-data /mnt/nextcloud-data
sudo chmod -R 0770 /mnt/nextcloud-data
```

## સ્ટેપ 8: નેક્સ્ટક્લાઉડ ઇન્સ્ટોલેશન પૂર્ણ કરો

તમારા વેબ બ્રાઉઝર ખોલો અને અહીં નેવિગેટ કરો:
- `http://your-pi-ip/nextcloud` અથવા 
- `http://your-pi-hostname/nextcloud`

જ્યારે પૂછવામાં આવે ત્યારે તમારું એડમિન એકાઉન્ટ બનાવો:
- યુઝરનેમ: એડમિન યુઝરનેમ પસંદ કરો
- પાસવર્ડ: એક મજબૂત પાસવર્ડ પસંદ કરો

"સ્ટોરેજ & ડેટાબેસ" પર ક્લિક કરો, પછી:
- ડેટા ફોલ્ડર: `/mnt/nextcloud-data`
- ડેટાબેસ કોન્ફિગર કરો: 
  - ડેટાબેસ પ્રકાર: MySQL/MariaDB
  - ડેટાબેસ યુઝર: `nextclouduser`
  - ડેટાબેસ પાસવર્ડ: (સ્ટેપ 4 માં તમે સેટ કરેલો પાસવર્ડ)
  - ડેટાબેસ નામ: `nextcloud`
  - ડેટાબેસ હોસ્ટ: `localhost`

ઇન્સ્ટોલેશન પૂર્ણ થવાની રાહ જુઓ અને "ફિનિશ સેટઅપ" પર ક્લિક કરો.

## સ્ટેપ 9: અનિવાર્ય પોસ્ટ-ઇન્સ્ટોલેશન કોન્ફિગરેશન

### ટ્રસ્ટેડ ડોમેન્સ કોન્ફિગર કરો

ડિફોલ્ટ રૂપે, નેક્સ્ટક્લાઉડ ફક્ત ઇન્સ્ટોલેશન દરમિયાન તમે વાપરેલા ડોમેનને જ ટ્રસ્ટ કરે છે. વધુ ઉમેરવા માટે:

```bash
sudo nano /var/www/nextcloud/config/config.php
```

`trusted_domains` એરે શોધો અને તમે વાપરશો તે બધા ડોમેન અને IP ઉમેરો:

```php
'trusted_domains' => 
array (
  0 => 'your-pi-ip',
  1 => 'your-domain.com',
  2 => 'your-pi.local',
),
```

### બેકગ્રાઉન્ડ ટાસ્ક્સ માટે ક્રોન જોબ્સ સેટ અપ કરો

બેટર પરફોર્મન્સ માટે, નેક્સ્ટક્લાઉડ બેકગ્રાઉન્ડ ટાસ્ક્સ માટે ક્રોન જોબ સેટ અપ કરો:

```bash
sudo crontab -u www-data -e
```

આ લાઇન ઉમેરો:

```
*/5 * * * * php -f /var/www/nextcloud/cron.php
```

પછી નેક્સ્ટક્લાઉડ એડમિન ઇન્ટરફેસમાં:
1. Settings > Administration > Basic settings પર જાઓ
2. Background jobs હેઠળ, "Cron" પસંદ કરો
3. "Save" પર ક્લિક કરો

### બેટર પરફોર્મન્સ માટે મેમરી કેશિંગ

ઇમ્પ્રુવ્ડ કેશિંગ માટે Redis ઇન્સ્ટોલ કરો:

```bash
sudo apt install -y redis-server php-redis
sudo systemctl enable redis-server
```

નેક્સ્ટક્લાઉડ કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /var/www/nextcloud/config/config.php
```

કોન્ફિગરેશન એરે અંદર આ લાઇન્સ ઉમેરો:

```php
'memcache.local' => '\\OC\\Memcache\\APCu',
'memcache.locking' => '\\OC\\Memcache\\Redis',
'redis' => [
     'host' => 'localhost',
     'port' => 6379,
],
```

સર્વિસીસ રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart apache2
sudo systemctl restart redis-server
```

## સ્ટેપ 10: HTTPS સક્ષમ કરો (ખૂબ ભલામણ કરેલ)

તમારા નેક્સ્ટક્લાઉડ ઇન્સ્ટન્સને HTTPS સાથે સુરક્ષિત કરો:

### Let's Encrypt માટે Certbot ઇન્સ્ટોલ કરો

```bash
sudo apt install -y certbot python3-certbot-apache
```

### ઇન્ટરનેટ-એક્સેસિબલ સર્વર માટે

જો તમારો સર્વર ડોમેન નામ સાથે ઇન્ટરનેટથી એક્સેસિબલ હોય:

```bash
sudo certbot --apache -d your-domain.com
```

પ્રક્રિયા પૂર્ણ કરવા માટે પ્રોમ્પ્ટનું પાલન કરો.

### ફક્ત લોકલ નેટવર્ક માટે

જો તમારો સર્વર ફક્ત તમારા લોકલ નેટવર્ક પર હોય, તો તમે સેલ્ફ-સાઇન્ડ સર્ટિફિકેટ બનાવી શકો છો:

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

તમારા Apache કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /etc/apache2/sites-available/nextcloud-ssl.conf
```

ઉમેરો:

```apache
<VirtualHost *:443>
    DocumentRoot /var/www/nextcloud/
    ServerName your-pi.local

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
    SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key

    <Directory /var/www/nextcloud/>
        Options +FollowSymlinks
        AllowOverride All
        Require all granted
        <IfModule mod_dav.c>
            Dav off
        </IfModule>
        SetEnv HOME /var/www/nextcloud
        SetEnv HTTP_HOME /var/www/nextcloud
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/nextcloud_error.log
    CustomLog ${APACHE_LOG_DIR}/nextcloud_access.log combined
</VirtualHost>
```

SSL મોડ્યુલ અને કોન્ફિગરેશન સક્ષમ કરો:

```bash
sudo a2enmod ssl
sudo a2ensite nextcloud-ssl
sudo systemctl restart apache2
```

### HTTPS રિડાયરેક્ટ ફોર્સ કરો

તમારા ઓરિજિનલ કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /etc/apache2/sites-available/nextcloud.conf
```

સામગ્રીને આનાથી બદલો:

```apache
<VirtualHost *:80>
    ServerName your-pi.local
    Redirect permanent / https://your-pi.local/
</VirtualHost>
```

Apache રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart apache2
```

## સ્ટેપ 11: બેટર સિક્યુરિટી માટે એડવાન્સ્ડ કોન્ફિગરેશન

### સિક્યુરિટી હેડર્સ ઉમેરો

તમારા SSL કોન્ફિગરેશન એડિટ કરો:

```bash
sudo nano /etc/apache2/sites-available/nextcloud-ssl.conf
```

`<VirtualHost>` સેક્શનની અંદર આ લાઇન્સ ઉમેરો:

```apache
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains"
    Header always set Referrer-Policy "no-referrer"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Download-Options "noopen"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Permitted-Cross-Domain-Policies "none"
    Header always set X-Robots-Tag "none"
    Header always set X-XSS-Protection "1; mode=block"
</IfModule>
```

Apache રિસ્ટાર્ટ કરો:

```bash
sudo a2enmod headers
sudo systemctl restart apache2
```

### સિક્યુરિટી સ્કેન ફિક્સીસ

નેક્સ્ટક્લાઉડ એડમિન પેનલથી સિક્યુરિટી સ્કેન ચલાવો અને તે ઓળખે તેવા કોઈપણ મુદ્દાઓને ફિક્સ કરો.

## સ્ટેપ 12: તમારા નેક્સ્ટક્લાઉડ એક્સેસ કરવું

હવે તમારો નેક્સ્ટક્લાઉડ સર્વર સેટઅપ થઈ ગયો છે, તમે તેને ઘણી રીતે એક્સેસ કરી શકો છો:

### વેબ ઇન્ટરફેસ

કોઈપણ બ્રાઉઝરમાં તમારા નેક્સ્ટક્લાઉડને એક્સેસ કરો:
- `https://your-pi-ip` અથવા 
- `https://your-domain.com`

### મોબાઇલ એપ્સ

ઓફિશિયલ નેક્સ્ટક્લાઉડ એપ્સ ડાઉનલોડ કરો:
- Android: [Google Play](https://play.google.com/store/apps/details?id=com.nextcloud.client) અથવા [F-Droid](https://f-droid.org/packages/com.nextcloud.client/)
- iOS: [App Store](https://apps.apple.com/app/nextcloud/id1125420102)

મોબાઇલ એપ્સમાં ઓટોમેટિક ફોટો/વિડિયો બેકઅપ કોન્ફિગર કરો.

### ડેસ્કટોપ ક્લાયન્ટ્સ

[નેક્સ્ટક્લાઉડ વેબસાઇટ](https://nextcloud.com/clients/)થી ડેસ્કટોપ સિંક ક્લાયન્ટ્સ ડાઉનલોડ કરો:
- Windows
- macOS
- Linux

## સ્ટેપ 13: મેઇન્ટેનન્સ અને મેનેજમેન્ટ

### ફાઇલ સ્કેનિંગ

જો તમે ડેટા ડિરેક્ટરીમાં સીધા ફાઇલ ઉમેરો છો, તો તમારે તેમને સ્કેન કરવાની જરૂર છે:

```bash
sudo -u www-data php /var/www/nextcloud/occ files:scan --all
```

### લોક્ડ ફાઇલ્સ ફિક્સ કરવી

જો તમને "files is locked" એરર મળે:

```bash
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --on
sudo mysql -u root -p -e "DELETE FROM nextcloud.oc_file_locks WHERE 1"
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --off
```

### નેક્સ્ટક્લાઉડ અપડેટ કરવું

```bash
# મેઇન્ટેનન્સ મોડ સક્ષમ કરો
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --on

# અપડેટ કરતા પહેલા બેકઅપ લો
sudo rsync -avh --delete /var/www/nextcloud/ /backup/nextcloud-$(date +%Y%m%d)/

# અપડેટર ચલાવો
sudo -u www-data php /var/www/nextcloud/updater/updater.phar

# મેઇન્ટેનન્સ મોડ અક્ષમ કરો
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --off
```

### ડેટાબેસ ઓપ્ટિમાઇઝેશન

પીરિયોડિકલી તમારા ડેટાબેસને ઓપ્ટિમાઇઝ કરો:

```bash
sudo -u www-data php /var/www/nextcloud/occ db:add-missing-indices
sudo -u www-data php /var/www/nextcloud/occ db:convert-filecache-bigint
```

## સ્ટેપ 14: પરફોર્મન્સ ઓપ્ટિમાઇઝેશન

### બેટર પરફોર્મન્સ માટે PHP-FPM

બિઝી નેક્સ્ટક્લાઉડ ઇન્સ્ટન્સીસ માટે, PHP-FPM પર સ્વિચ કરો:

```bash
# PHP-FPM ઇન્સ્ટોલ કરો
sudo apt install -y php-fpm

# Apache પ્રોક્સી મોડ્યુલ્સ સક્ષમ કરો
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf php*-fpm

# સર્વિસીસ રિસ્ટાર્ટ કરો
sudo systemctl restart php*-fpm
sudo systemctl restart apache2
```

### એડિશનલ ઇન્ડેક્સ પરફોર્મન્સ

મોટા ઇન્સ્ટોલેશન માટે, `config.php` માં આ ઉમેરવાનું વિચારો:

```php
'filelocking.enabled' => true,
'memcache.distributed' => '\\OC\\Memcache\\Redis',
```

## સ્ટેપ 15: તમારા નેક્સ્ટક્લાઉડને એન્હાન્સ કરવું

ફંક્શનાલિટી વધારવા માટે નેક્સ્ટક્લાઉડ એપ ઇકોસિસ્ટમ એક્સપ્લોર કરો:

### વિચારવા લાયક લોકપ્રિય એપ્સ

1. **Collabora Online**: ફુલ ઓફિસ સ્યુટ ઇન્ટિગ્રેશન
   ```bash
   sudo docker run -t -d -p 9980:9980 -e "domain=your-domain-or-ip" --restart always collabora/code
   ```

2. **Talk**: વિડિયો કોન્ફરન્સિંગ અને ચેટ
   - નેક્સ્ટક્લાઉડ એપ સ્ટોરમાંથી ઇન્સ્ટોલ કરો

3. **Calendar & Contacts**: બધા ડિવાઇસ પર સિંક
   - નેક્સ્ટક્લાઉડ એપ સ્ટોરમાંથી ઇન્સ્ટોલ કરો

4. **Notes**: સિંક્રોનાઇઝ્ડ નોટ-ટેકિંગ
   - નેક્સ્ટક્લાઉડ એપ સ્ટોરમાંથી ઇન્સ્ટોલ કરો

5. **News**: RSS ફીડ રીડર
   - નેક્સ્ટક્લાઉડ એપ સ્ટોરમાંથી ઇન્સ્ટોલ કરો

## ટ્રબલશૂટિંગ

### લોગ્સ ચેક કરવા

સમસ્યાઓનું ટ્રબલશૂટિંગ કરતી વખતે, આ લોગ્સ ચેક કરો:

```bash
# Apache એરર લોગ્સ
sudo tail -f /var/log/apache2/error.log

# નેક્સ્ટક્લાઉડ લોગ્સ
sudo tail -f /var/www/nextcloud/data/nextcloud.log
```

### પરમિશન સમસ્યાઓ

જો તમને પરમિશન સમસ્યાઓનો સામનો કરવો પડે:

```bash
sudo chown -R www-data:www-data /var/www/nextcloud
sudo chown -R www-data:www-data /mnt/nextcloud-data

# યોગ્ય પરમિશન સેટ કરો
sudo find /var/www/nextcloud/ -type d -exec chmod 750 {} \;
sudo find /var/www/nextcloud/ -type f -exec chmod 640 {} \;
sudo chmod -R 770 /mnt/nextcloud-data
```

### PHP મેમરી લિમિટ્સ વધારવી

જો તમને મેમરી એરર મળે:

```bash
sudo nano /etc/php/*/apache2/conf.d/99-nextcloud.ini
```

આ વેલ્યુ વધારો:
```
memory_limit = 1024M
```

### ધીમા પરફોર્મન્સ

ધીમા નેક્સ્ટક્લાઉડ પરફોર્મન્સ માટે:

1. તમારી ડ્રાઇવ સ્પીડ ચેક કરો:
   ```bash
   sudo hdparm -t /dev/sdX
   ```

2. ફાસ્ટર સ્ટોરેજ ડિવાઇસ (SSD) પર સ્વિચ કરવાનું વિચારો

3. તમારા રાસ્પબેરી પાઈ મોડેલ માટે ઉપલબ્ધ હોય તો વધારાના RAM ઉમેરો

## બેકઅપ સ્ટ્રેટેજી

### નિયમિત ઓટોમેટેડ બેકઅપ્સ

બેકઅપ સ્ક્રિપ્ટ બનાવો:

```bash
sudo nano /home/pi/nextcloud-backup.sh
```

ઉમેરો:

```bash
#!/bin/bash
BACKUP_DIR="/path/to/backup/location"
DATE=$(date +"%Y%m%d")

# બેકઅપ ડિરેક્ટરી બનાવો
mkdir -p $BACKUP_DIR/$DATE

# મેઇન્ટેનન્સ મોડ સક્ષમ કરો
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --on

# ડેટાબેસ બેકઅપ કરો
sudo mysqldump --single-transaction -u root -p$(cat /root/.mysql_password) nextcloud > $BACKUP_DIR/$DATE/nextcloud-db.sql

# કોન્ફિગ અને ડેટા બેકઅપ કરો
sudo rsync -avh /var/www/nextcloud/config/ $BACKUP_DIR/$DATE/config/
sudo rsync -avh /mnt/nextcloud-data/ $BACKUP_DIR/$DATE/data/

# મેઇન્ટેનન્સ મોડ અક્ષમ કરો
sudo -u www-data php /var/www/nextcloud/occ maintenance:mode --off

# 30 દિવસથી જૂના બેકઅપ્સ ડિલીટ કરો
find $BACKUP_DIR/* -type d -mtime +30 -exec rm -rf {} \;
```

તેને એક્ઝિક્યુટેબલ બનાવો અને શેડ્યૂલ કરો:

```bash
chmod +x /home/pi/nextcloud-backup.sh
sudo crontab -e
```

ઉમેરો:
```
0 2 * * 0 /home/pi/nextcloud-backup.sh > /home/pi/backup.log 2>&1
```

## નિષ્કર્ષ

તમારો રાસ્પબેરી પાઈ હવે સંપૂર્ણ, સુરક્ષિત અને ઓપ્ટિમાઇઝ કરેલા નેક્સ્ટક્લાઉડ સર્વર ચલાવી રહ્યો છે, તમને આપતું:

- તમારા ડેટા અને પ્રાઇવસી પર સંપૂર્ણ નિયંત્રણ
- તમારા બધા ડિવાઇસથી સીમલેસ ફાઇલ એક્સેસ
- ઓટોમેટિક ફોટો અને વિડિયો બેકઅપ્સ
- મીડિયા સ્ટ્રીમિંગ ક્ષમતાઓ
- કોલાબોરેશન ટૂલ્સ
- હાઇલી એક્સપેન્ડેબલ પ્લેટફોર્મ

આ સેલ્ફ-હોસ્ટેડ સોલ્યુશન કમર્શિયલ ક્લાઉડ સર્વિસીસની બધી સુવિધા પ્રદાન કરે છે પરંતુ વધારેલી પ્રાઇવસી, કોઈ સબ્સ્ક્રિપ્શન ફી નહીં, અને તમારા ફિઝિકલ ડ્રાઇવ્સ સિવાય કોઈ સ્ટોરેજ મર્યાદા નહીં તે સાથે.

તમારા સર્વરને સુરક્ષિત અને અપ-ટુ-ડેટ રાખવા માટે નિયમિતપણે નેક્સ્ટક્લાઉડ અપડેટ્સ અને સિક્યુરિટી જાહેરાતો માટે ચેક કરો. વધારાના સપોર્ટ અને ટિપ્સ માટે નેક્સ્ટક્લાઉડ કમ્યુનિટી ફોરમમાં જોડાઓ.

તમારા પર્સનલ ક્લાઉડ સર્વરનો આનંદ માણો!
