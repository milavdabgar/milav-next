---
title: "રાસ્પબેરી પાઈ પર ઓનક્લાઉડ સાથે તમારું પર્સનલ ક્લાઉડ સ્ટોરેજ બનાવવું"
date: 2025-03-05
description: "રાસ્પબેરી પાઈ પર ઓનક્લાઉડનો ઉપયોગ કરીને તમારું પોતાનું પ્રાઇવેટ ક્લાઉડ સ્ટોરેજ સોલ્યુશન બનાવવા માટેની વિસ્તૃત ટ્યુટોરિયલ"
summary: "શીખો કેવી રીતે તમારા રાસ્પબેરી પાઈને ઓટોમેટિક બેકઅપ, ફાઇલ સિંકિંગ, મીડિયા સ્ટ્રીમિંગ અને વધુ સાથે શક્તિશાળી પ્રાઇવેટ ક્લાઉડ સર્વરમાં પરિવર્તિત કરવું."
tags: ["raspberry pi", "owncloud", "self-hosted", "cloud storage", "server", "privacy", "linux", "tutorial"]
---

રાસ્પબેરી પાઈ પર ઓનક્લાઉડ ચલાવીને તમારા ડિજિટલ જીવન પર નિયંત્રણ મેળવો. આ વિસ્તૃત ગાઇડ તમને ડ્રોપબોક્સ, ગૂગલ ડ્રાઇવ અથવા વનડ્રાઇવ જેવી કમર્શિયલ સેવાઓના સેલ્ફ-હોસ્ટેડ વિકલ્પ બનાવવામાં મદદ કરશે, જે તમને તમારા ડેટા પર સંપૂર્ણ નિયંત્રણ આપશે.

## ઓનક્લાઉડ શા માટે?

ઓનક્લાઉડ સેલ્ફ-હોસ્ટેડ ક્લાઉડ સોલ્યુશન તરીકે કેટલાક કારણોસર ઉત્કૃષ્ટ છે:

- **સંપૂર્ણ ડેટા માલિકી**: તમારી ફાઇલો તમારા હાર્ડવેર પર તમારા નિયંત્રણ હેઠળ રહે છે
- **વધારેલ પ્રાઇવસી**: કોઈ થર્ડ-પાર્ટી કંપનીઓ તમારા ડેટાનું વિશ્લેષણ કરતી નથી
- **કોસ્ટ-ઇફેક્ટિવ**: ઇનિશિયલ સેટઅપ પછી કોઈ મંથલી સબ્સ્ક્રિપ્શન ફી નહીં
- **કસ્ટમાઇઝેબલ સ્ટોરેજ**: મોટા ડ્રાઇવ્સ કનેક્ટ કરીને કેપેસિટી વધારો
- **વર્સેટાઇલ ફાઇલ એક્સેસ**: ડેસ્કટોપ અને મોબાઇલ એપ્સ સાથે બધા ડિવાઇસ પર સિંક કરો
- **પાવરફુલ શેરિંગ ફીચર્સ**: કસ્ટમ પરમિશન્સ સાથે ફાઇલ્સ અને ફોલ્ડર્સ શેર કરો
- **રિચ ઇકોસિસ્ટમ**: કેલેન્ડર, કોન્ટેક્ટ્સ અને વધુ માટે પ્લગઇન્સ સાથે ફંક્શનાલિટી વધારો

## પૂર્વાપેક્ષાઓ

- રાસ્પબેરી પાઈ 4 (4GB+ RAM રેકમેન્ડેડ) અથવા રાસ્પબેરી પાઈ 5
- રાસ્પબેરી પાઈ OS (બેટર પરફોર્મન્સ માટે 64-બિટ રેકમેન્ડેડ)
- એક્સટર્નલ સ્ટોરેજ ડિવાઇસ (પરફોર્મન્સ માટે HDD કરતાં SSD રેકમેન્ડેડ)
- તમારા લોકલ નેટવર્ક પર સ્ટેટિક IP અથવા રિમોટ એક્સેસ માટે ડાયનેમિક DNS
- લિનક્સ કમાન્ડ લાઇનની બેઝિક જાણકારી

## સ્ટેપ 1: તમારી સિસ્ટમ અપડેટ કરો

તમારી સિસ્ટમમાં લેટેસ્ટ સિક્યોરિટી પેચ છે તેની ખાતરી કરવા માટે ફ્રેશ અપડેટથી શરૂ કરો:

```bash
sudo apt update && sudo apt full-upgrade -y
sudo reboot
```

## સ્ટેપ 2: વેબ સર્વર અને PHP ઇન્સ્ટોલ કરો

અપાચે, MariaDB (MySQL), અને જરૂરી એક્સટેન્શન્સ સાથે PHP ઇન્સ્ટોલ કરો:

```bash
sudo apt install -y apache2 mariadb-server libapache2-mod-php
sudo apt install -y php-gd php-json php-mysql php-curl php-mbstring
sudo apt install -y php-intl php-imagick php-xml php-zip php-bcmath
```

બૂટ પર ચાલવા માટે અપાચે અને MariaDB શરૂ કરો અને એનેબલ કરો:

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

## સ્ટેપ 3: ઓપ્ટિમલ પરફોર્મન્સ માટે PHP કોન્ફિગર કરો

ઓનક્લાઉડ માટે PHP પરફોર્મન્સ વધારવા માટે કસ્ટમ કોન્ફિગરેશન બનાવો:

```bash
sudo nano /etc/php/$(php -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')/apache2/conf.d/99-owncloud.ini
```

આ ઓપ્ટિમાઇઝ્ડ સેટિંગ્સ ઉમેરો:

```
memory_limit = 512M
upload_max_filesize = 1024M
post_max_size = 1024M
max_execution_time = 300
max_input_time = 300
date.timezone = Europe/London  # તમારા ટાઇમઝોન અનુસાર બદલો
opcache.enable = 1
opcache.memory_consumption = 128
opcache.interned_strings_buffer = 8
opcache.max_accelerated_files = 10000
```

ફેરફારો લાગુ કરવા માટે અપાચે રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart apache2
```

## સ્ટેપ 4: MariaDB ડેટાબેસ કોન્ફિગર કરો

તમારા MariaDB ઇન્સ્ટોલેશનને સિક્યોર કરો:

```bash
sudo mysql_secure_installation
```

રૂટ પાસવર્ડ સેટ કરવા અને તમારા ઇન્સ્ટોલેશનને સિક્યોર કરવા માટે પ્રોમ્પ્ટ્સને અનુસરો (સામાન્ય રીતે બધા પ્રશ્નોના "Y" જવાબ આપો).

ઓનક્લાઉડ માટે ડેડિકેટેડ ડેટાબેસ બનાવો:

```bash
sudo mysql -u root -p
```

એકવાર લોગ થઈ જાય, પછી યોગ્ય પરમિશન્સ સાથે ડેટાબેસ અને યુઝર બનાવો:

```sql
CREATE DATABASE owncloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'ownclouduser'@'localhost' IDENTIFIED BY 'your-secure-password';
GRANT ALL PRIVILEGES ON owncloud.* TO 'ownclouduser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## સ્ટેપ 5: ઓનક્લાઉડ ડાઉનલોડ અને ઇન્સ્ટોલ કરો

ઓનક્લાઉડની લેટેસ્ટ વર્ઝન ડાઉનલોડ કરો:

```bash
cd /tmp
wget https://download.owncloud.org/community/owncloud-complete-latest.tar.bz2
```

એક્સટ્રેક્ટ કરો અને વેબ ડિરેક્ટરીમાં મૂવ કરો:

```bash
sudo tar -xjf owncloud-complete-latest.tar.bz2
sudo mv owncloud /var/www/
sudo chown -R www-data:www-data /var/www/owncloud/
```

## સ્ટેપ 6: ઓનક્લાઉડ માટે અપાચે કોન્ફિગર કરો

ઓનક્લાઉડ માટે ડેડિકેટેડ અપાચે કોન્ફિગરેશન ફાઇલ બનાવો:

```bash
sudo nano /etc/apache2/sites-available/owncloud.conf
```

ઓપ્ટિમલ સિક્યોરિટી અને પરફોર્મન્સ માટે નીચેની સામગ્રી ઉમેરો:

```apache
Alias /owncloud "/var/www/owncloud/"

<Directory /var/www/owncloud/>
  Options +FollowSymlinks
  AllowOverride All

  <IfModule mod_dav.c>
    Dav off
  </IfModule>

  SetEnv HOME /var/www/owncloud
  SetEnv HTTP_HOME /var/www/owncloud
  
  # મોડર્ન સિક્યોરિટી હેડર્સ
  <IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set Referrer-Policy "no-referrer"
  </IfModule>
</Directory>

# HTTP/2 એનેબલ કરો બેટર પરફોર્મન્સ માટે
<IfModule mod_http2.c>
    Protocols h2 h2c http/1.1
</IfModule>
```

કોન્ફિગરેશન અને જરૂરી અપાચે મોડ્યુલ્સ એનેબલ કરો:

```bash
sudo ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf
sudo a2enmod headers env dir mime rewrite ssl http2
sudo systemctl restart apache2
```

## સ્ટેપ 7: એક્સટર્નલ સ્ટોરેજ સેટ અપ કરો

### તમારા એક્સટર્નલ ડ્રાઇવને માઉન્ટ કરો

સૌ પ્રથમ, તમારા ડ્રાઇવને ઓળખો:

```bash
lsblk
```

ડેડિકેટેડ માઉન્ટ પોઇન્ટ બનાવો:

```bash
sudo mkdir -p /mnt/owncloud-data
```

વિવિધ ફાઇલસિસ્ટમ પ્રકારો માટે, જરૂરી સપોર્ટ ઇન્સ્ટોલ કરો:

```bash
# NTFS ફોર્મેટેડ ડ્રાઇવ્સ માટે
sudo apt install ntfs-3g -y

# exFAT ફોર્મેટેડ ડ્રાઇવ્સ માટે
sudo apt install exfat-fuse exfat-utils -y
```

વિશ્વસનીય માઉન્ટિંગ માટે તમારા ડ્રાઇવના UUID શોધો:

```bash
sudo blkid
```

ફાઇલસિસ્ટમ ટેબલ (fstab) એડિટ કરીને ઓટોમેટિક માઉન્ટિંગ સેટ કરો:

```bash
sudo nano /etc/fstab
```

તમારા ડ્રાઇવની ફાઇલસિસ્ટમના આધારે એક લાઇન ઉમેરો:

```
# ext4 ફાઇલસિસ્ટમ માટે (લિનક્સ માટે રેકમેન્ડેડ)
UUID=your-uuid-here /mnt/owncloud-data ext4 defaults,noatime 0 0

# NTFS ફાઇલસિસ્ટમ માટે
UUID=your-uuid-here /mnt/owncloud-data ntfs-3g defaults,permissions,uid=www-data,gid=www-data,noatime 0 0

# exFAT ફાઇલસિસ્ટમ માટે
UUID=your-uuid-here /mnt/owncloud-data exfat defaults,uid=www-data,gid=www-data,noatime 0 0
```

ડ્રાઇવ માઉન્ટ કરો અને વેરિફાય કરો:

```bash
sudo mount -a
df -h | grep owncloud-data
```

સાચા પરમિશન્સ સેટ કરો:

```bash
sudo chown -R www-data:www-data /mnt/owncloud-data
sudo chmod -R 770 /mnt/owncloud-data
```

## સ્ટેપ 8: ઓનક્લાઉડ વેબ સેટઅપ પૂર્ણ કરો

તમારા વેબ બ્રાઉઝરને ખોલો અને `http://your-pi-ip/owncloud` પર નેવિગેટ કરો અથવા જો તમે પાઈ પર લોકલી એક્સેસ કરી રહ્યા છો, તો `http://localhost/owncloud` નો ઉપયોગ કરો.

તમારું એડમિન એકાઉન્ટ બનાવો અને ડેટાબેસ કનેક્શન કોન્ફિગર કરો:

- એડમિન યુઝરનેમ: એક મજબૂત યુઝરનેમ પસંદ કરો
- એડમિન પાસવર્ડ: સિક્યોર પાસવર્ડનો ઉપયોગ કરો (મિક્સ્ડ કેસ, નંબર્સ, સિમ્બોલ્સ સાથે 12+ અક્ષરો)
- ડેટા ફોલ્ડર: `/mnt/owncloud-data` (એક્સટર્નલ સ્ટોરેજ પર બેટર પરફોર્મન્સ માટે)
- ડેટાબેસ ટાઇપ: MySQL/MariaDB
- ડેટાબેસ યુઝર: ownclouduser
- ડેટાબેસ પાસવર્ડ: your-secure-password (સ્ટેપ 4 માંથી)
- ડેટાબેસ નેમ: owncloud
- ડેટાબેસ હોસ્ટ: localhost

ઇન્સ્ટોલેશન પૂર્ણ કરવા માટે "Finish setup" પર ક્લિક કરો.

## સ્ટેપ 9: આવશ્યક પોસ્ટ-ઇન્સ્ટોલેશન કોન્ફિગરેશન

### ટ્રસ્ટેડ ડોમેન્સ કોન્ફિગર કરો

મંજૂર ડોમેન નામો સ્પષ્ટ કરવા માટે ઓનક્લાઉડ કોન્ફિગરેશન ફાઇલ એડિટ કરો:

```bash
sudo nano /var/www/owncloud/config/config.php
```

`trusted_domains` એરેને શોધો અને તમારા પાઈનું IP એડ્રેસ અને કોઈપણ ડોમેન નામ ઉમેરો:

```php
'trusted_domains' => 
array (
  0 => 'localhost',
  1 => 'your-pi-ip',  // દા.ત., 192.168.1.100
  2 => 'your-domain.com',
  3 => 'cloud.yourdomain.com',
),
```

### બેકગ્રાઉન્ડ જોબ્સ સેટ અપ કરો

ઓપ્ટિમલ પરફોર્મન્સ માટે, સિસ્ટમ ક્રોન જોબ કોન્ફિગર કરો:

```bash
sudo crontab -u www-data -e
```

દર 15 મિનિટે ઓનક્લાઉડ મેઇન્ટેનન્સ ટાસ્ક્સ ચલાવવા માટે આ લાઇન ઉમેરો:

```
*/15 * * * * php -f /var/www/owncloud/cron.php > /dev/null 2>&1
```

ઓનક્લાઉડ એડમિન સેટિંગ્સમાં (Settings → Admin → General), બેકગ્રાઉન્ડ જોબ્સ મેથડને "Cron" માં બદલો.

## સ્ટેપ 10: HTTPS એનેબલ કરો (સિક્યોરિટી માટે આવશ્યક)

સિક્યોર રિમોટ એક્સેસ માટે, Let's Encrypt સર્ટિફિકેટ્સ સાથે HTTPS સેટ કરો:

```bash
sudo apt install certbot python3-certbot-apache -y
```

જો તમારી પાસે તમારા રાસ્પબેરી પાઈ તરફ પોઇન્ટ કરતું ડોમેન નેમ છે:

```bash
sudo certbot --apache -d your-domain.com
```

સેટઅપ પૂર્ણ કરવા માટે પ્રોમ્પ્ટ્સને અનુસરો અને HTTP ટ્રાફિકને HTTPS પર રીડાયરેક્ટ કરવાનું પસંદ કરો.

ફક્ત લોકલ નેટવર્ક ઉપયોગ માટે, તમે સેલ્ફ-સાઇન્ડ સર્ટિફિકેટ બનાવી શકો છો:

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/owncloud-selfsigned.key -out /etc/ssl/certs/owncloud-selfsigned.crt
```

પછી અપાચેને તેનો ઉપયોગ કરવા માટે કોન્ફિગર કરો:

```bash
sudo nano /etc/apache2/sites-available/owncloud-ssl.conf
```

તમારા મૌજૂદા કોન્ફિગરેશન જેવું જ પરંતુ SSL સેટિંગ્સ સાથે એક કોન્ફિગરેશન ઉમેરો, પછી તેને એનેબલ કરો:

```bash
sudo a2ensite owncloud-ssl.conf
sudo systemctl restart apache2
```

## સ્ટેપ 11: ગમે ત્યાંથી તમારા ઓનક્લાઉડને એક્સેસ કરવું

હવે તમે એકાધિક પદ્ધતિઓ દ્વારા તમારા ઓનક્લાઉડને એક્સેસ કરી શકો છો:

- **વેબ બ્રાઉઝર**: `https://your-domain.com/owncloud` અથવા `https://your-pi-ip/owncloud` પર નેવિગેટ કરો
- **ડેસ્કટોપ સિંક ક્લાયન્ટ**: 
  - [owncloud.com/download](https://owncloud.com/download/) પરથી ડાઉનલોડ કરો
  - Windows, macOS, અથવા Linux પર ઇન્સ્ટોલ કરો
  - તમારા સર્વર URL અને લોગિન ક્રેડન્શિયલ્સનો ઉપયોગ કરીને કનેક્ટ કરો
  - સિંક કરવા માટે ફોલ્ડર્સ પસંદ કરો
- **મોબાઇલ એપ્સ**: 
  - Android (Google Play Store) અને iOS (App Store) માટે ઉપલબ્ધ
  - ઓટોમેટિક ફોટો અપલોડ્સ એનેબલ કરો
  - ચાલતા-ફરતા ડોક્યુમેન્ટ્સ એક્સેસ કરો

## સ્ટેપ 12: પરફોર્મન્સ ઓપ્ટિમાઇઝેશન

### ફાસ્ટર એક્સેસ માટે મેમરી કેશ

એફિશિયન્ટ કેશિંગ માટે Redis ઇન્સ્ટોલ કરો:

```bash
sudo apt install redis-server php-redis -y
sudo systemctl enable redis-server
```

Redis નો ઉપયોગ કરવા માટે ઓનક્લાઉડ કોન્ફિગ એડિટ કરો:

```bash
sudo nano /var/www/owncloud/config/config.php
```

ક્લોઝિંગ `);` પહેલા આ લાઇન્સ ઉમેરો:

```php
'memcache.local' => '\OC\Memcache\Redis',
'memcache.locking' => '\OC\Memcache\Redis',
'redis' => [
     'host' => 'localhost',
     'port' => 6379,
],
```

અપાચે રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart apache2
```

### ફાઇલ સિસ્ટમ કેશ

મોટી ફાઇલો સાથે બેટર પરફોર્મન્સ માટે:

```bash
sudo nano /var/www/owncloud/config/config.php
```

ઉમેરો:

```php
'filelocking.enabled' => true,
'filesystem_check_changes' => 1,
```

### ડેટાબેસ ઓપ્ટિમાઇઝેશન

ડેટાબેસ પરફોર્મન્સ ઓપ્ટિમાઇઝ કરવા માટે આ કમાન્ડ્સ પીરિયોડિકલી ચલાવો:

```bash
sudo -u www-data php /var/www/owncloud/occ db:convert-filecache-bigint
sudo -u www-data php /var/www/owncloud/occ db:add-missing-indices
```

## સ્ટેપ 13: ઓટોમેટેડ મેઇન્ટેનન્સ

### ઓટોમેટેડ બેકઅપ્સ

એક કોમ્પ્રિહેન્સિવ બેકઅપ સ્ક્રિપ્ટ બનાવો:

```bash
sudo nano /home/pi/owncloud-backup.sh
```

આ એન્હાન્સ્ડ કન્ટેન્ટ ઉમેરો:

```bash
#!/bin/bash
# રિટેન્શન સાથે ઓનક્લાઉડ બેકઅપ સ્ક્રિપ્ટ

# કોન્ફિગરેશન
BACKUP_DIR="/path/to/backup"
RETENTION_DAYS=14
DATE=$(date +"%Y-%m-%d")
BACKUP_NAME="owncloud_$DATE"
FULL_BACKUP_PATH="$BACKUP_DIR/$BACKUP_NAME"

# બેકઅપ ડિરેક્ટરી બનાવો
mkdir -p $FULL_BACKUP_PATH

# સ્ટાર્ટ ટાઇમ લોગ કરો
echo "Backup started at $(date)" > $FULL_BACKUP_PATH/backup.log

# ઓનક્લાઉડને મેઇન્ટેનન્સ મોડમાં મૂકો
echo "Enabling maintenance mode..." >> $FULL_BACKUP_PATH/backup.log
sudo -u www-data php /var/www/owncloud/occ maintenance:mode --on

# ડેટાબેસ બેકઅપ
echo "Backing up database..." >> $FULL_BACKUP_PATH/backup.log
sudo mysqldump --single-transaction -u root -p'your-database-password' owncloud > $FULL_BACKUP_PATH/owncloud-db.sql

# કોન્ફિગ અને ડેટા બેકઅપ
echo "Backing up config files..." >> $FULL_BACKUP_PATH/backup.log
sudo cp -r /var/www/owncloud/config $FULL_BACKUP_PATH/
echo "Backing up data files..." >> $FULL_BACKUP_PATH/backup.log
sudo rsync -avz --info=progress2 /mnt/owncloud-data/ $FULL_BACKUP_PATH/data/

# મેઇન્ટેનન્સ મોડની બહાર નીકળો
echo "Disabling maintenance mode..." >> $FULL_BACKUP_PATH/backup.log
sudo -u www-data php /var/www/owncloud/occ maintenance:mode --off

# બેકઅપ કમ્પ્રેસ કરો
echo "Compressing backup..." >> $FULL_BACKUP_PATH/backup.log
tar -czf $BACKUP_DIR/$BACKUP_NAME.tar.gz -C $BACKUP_DIR $BACKUP_NAME
rm -rf $FULL_BACKUP_PATH

# જૂના બેકઅપ દૂર કરો
echo "Cleaning up old backups..." >> $BACKUP_DIR/cleanup.log
find $BACKUP_DIR -name "owncloud_*.tar.gz" -type f -mtime +$RETENTION_DAYS -delete

echo "Backup completed: $BACKUP_DIR/$BACKUP_NAME.tar.gz" | tee -a $BACKUP_DIR/backup_history.log
```

તેને એક્ઝિક્યુટેબલ બનાવો:

```bash
chmod +x /home/pi/owncloud-backup.sh
```

સાપ્તાહિક બેકઅપ માટે crontab માં ઉમેરો:

```bash
crontab -e
```

ઉમેરો:

```
0 2 * * 0 /home/pi/owncloud-backup.sh
```

### ઓટોમેટિક અપડેટ્સ ચેક

ઓનક્લાઉડ અપડેટ્સ ચેક કરવા માટે એક સ્ક્રિપ્ટ બનાવો:

```bash
sudo nano /home/pi/check-owncloud-updates.sh
```

ઉમેરો:

```bash
#!/bin/bash
# ઓનક્લાઉડ અપડેટ્સ માટે ચેક કરો અને નોટિફાય કરો

UPDATE_INFO=$(sudo -u www-data php /var/www/owncloud/occ update:check)

if [[ $UPDATE_INFO == *"Update to"* ]]; then
  echo "OwnCloud update available: $UPDATE_INFO" | mail -s "OwnCloud Update Available" your-email@example.com
fi
```

તેને સાપ્તાહિક ચલાવવાનું શેડ્યૂલ કરો:

```
0 8 * * 1 /home/pi/check-owncloud-updates.sh
```

## સિક્યોરિટી હાર્ડનિંગ

### Fail2Ban ઇન્ટિગ્રેશન

બ્રુટ ફોર્સ એટેક્સથી સુરક્ષા માટે Fail2Ban ઇન્સ્ટોલ કરો:

```bash
sudo apt install fail2ban -y
sudo nano /etc/fail2ban/filter.d/owncloud.conf
```

ફિલ્ટર કોન્ફિગરેશન બનાવો:

```
[Definition]
failregex = ^{"reqId":".*","level":2,"time":".*","remoteAddr":".*","user":".*","app":"core","method":".*","url":".*","message":"Login failed: '.*' \(Remote IP: '<HOST>'\)"}$
ignoreregex =
```

જેલ કોન્ફિગર કરો:

```bash
sudo nano /etc/fail2ban/jail.d/owncloud.conf
```

ઉમેરો:

```
[owncloud]
enabled = true
port = 80,443
filter = owncloud
logpath = /var/www/owncloud/data/owncloud.log
maxretry = 3
bantime = 86400
findtime = 600
```

Fail2Ban રિસ્ટાર્ટ કરો:

```bash
sudo systemctl restart fail2ban
```

### વધારાના સિક્યોરિટી મેઝર્સ

વધુ પ્રતિબંધિત `.htaccess` ફાઇલ બનાવો:

```bash
sudo nano /var/www/owncloud/.htaccess
```

ટોપ પર આ રૂલ્સ ઉમેરો:

```apache
# ડિરેક્ટરી લિસ્ટિંગ ડિસેબલ કરો
Options -Indexes

# સેન્સિટિવ ફાઇલોના એક્સેસને બ્લોક કરો
<FilesMatch "^\.(?!well-known)|~$|^#.*#$|\.bak$|\.dist$|\.orig$|\.save$|config.php$">
  <IfModule mod_authz_core.c>
    Require all denied
  </IfModule>
</FilesMatch>
```

## એડવાન્સ્ડ ફીચર્સ અને કસ્ટમાઇઝેશન

### એડિશનલ એપ્સ ઇન્સ્ટોલ કરવી

ઓનક્લાઉડ ફંક્શનાલિટી વધારવા માટે વિવિધ એપ્સ ઓફર કરે છે:

1. તમારા ઓનક્લાઉડ વેબ ઇન્ટરફેસમાં લોગ ઇન કરો
2. ટોપ-રાઇટ કોર્નરમાં તમારા યુઝરનેમ પર ક્લિક કરો અને "Apps" પસંદ કરો
3. "Available apps" સેક્શન બ્રાઉઝ કરો
4. તમે ઇન્સ્ટોલ કરવા માંગતા હો તે કોઈપણ એપ્સ પર "Enable" પર ક્લિક કરો

લોકપ્રિય એપ્સમાં શામેલ છે:
- **Calendar**: ઇવેન્ટ્સ મેનેજ કરો અને રિમાઇન્ડર સેટ કરો
- **Contacts**: તમારું એડ્રેસ બુક સ્ટોર અને સિંક કરો
- **Documents**: કોલેબોરેટિવ ડોક્યુમેન્ટ એડિટિંગ
- **Music**: તમારા મ્યુઝિક કલેક્શનને સ્ટ્રીમ કરો
- **Gallery**: એન્હાન્સ્ડ ફોટો વ્યુઇંગ એક્સપીરિયન્સ
- **Bookmarks**: ડિવાઇસ આખે બ્રાઉઝર બુકમાર્ક્સ સિંક કરો

### ફાઇલ વર્ઝનિંગ એનેબલ કરવું

ઓનક્લાઉડ ફાઇલ ચેન્જિસનો ટ્રેક રાખી શકે છે, જેનાથી તમે અગાઉના વર્ઝન રિસ્ટોર કરી શકો છો:

1. એડમિન તરીકે લોગ ઇન કરો
2. Settings → Admin → Additional પર જાઓ
3. "Versions" એનેબલ કરો અને રિટેન્શન સેટિંગ્સ કોન્ફિગર કરો:
   - વર્ઝન્સની મહત્તમ સંખ્યા: 50 (જરૂરિયાત મુજબ એડજસ્ટ કરો)
   - વર્ઝન્સ માટે મહત્તમ ઉંમર: 180 દિવસ (જરૂરિયાત મુજબ એડજસ્ટ કરો)

### એક્સટર્નલ સ્ટોરેજ ઇન્ટિગ્રેશન

તમારા ઓનક્લાઉડને એક્સટર્નલ સ્ટોરેજ સર્વિસિસ સાથે કનેક્ટ કરો:

1. "External storage support" એપ એનેબલ કરો
2. Settings → Admin → Storage પર જાઓ
3. એક્સટર્નલ સ્ટોરેજ સોર્સિસ કોન્ફિગર કરો:
   - **Local**: તમારા સર્વર પર વધારાના ફોલ્ડર્સ
   - **External**: FTP, SFTP, WebDAV, Samba શેર્સ
   - **Cloud**: Amazon S3, Google Drive, Dropbox

## સામાન્ય સમસ્યાઓનું નિવારણ

### પરમિશન સમસ્યાઓ

જો તમને પરમિશન સમસ્યાઓનો સામનો કરવો પડે છે:

```bash
sudo chown -R www-data:www-data /var/www/owncloud
sudo chown -R www-data:www-data /mnt/owncloud-data
sudo find /var/www/owncloud/ -type d -exec chmod 750 {} \;
sudo find /var/www/owncloud/ -type f -exec chmod 640 {} \;
```

### કનેક્શન સમસ્યાઓ

જો તમે ઓનક્લાઉડ સાથે કનેક્ટ ન કરી શકો:

1. અપાચે સ્ટેટસ ચેક કરો: `sudo systemctl status apache2`
2. અપાચે એરર લોગ્સ રિવ્યુ કરો: `sudo tail -f /var/log/apache2/error.log`
3. ઓનક્લાઉડ લોગ્સ ચેક કરો: `sudo tail -f /var/www/owncloud/data/owncloud.log`
4. ફાયરવોલ સેટિંગ્સ વેરિફાય કરો: `sudo ufw status`
5. પોર્ટ્સ ખુલ્લા છે તેની ખાતરી કરો: `sudo ufw allow 80/tcp` અને `sudo ufw allow 443/tcp`

### ફાઇલ અપલોડ સમસ્યાઓ

જો તમે મોટી ફાઇલો અપલોડ ન કરી શકો:

1. તમારી કસ્ટમ PHP ini ફાઇલમાં PHP સેટિંગ્સ ચેક કરો
2. અપાચે ટાઇમઆઉટ સેટિંગ્સ વેરિફાય કરો
3. ઓનક્લાઉડના config.php માં મેક્સ ફાઇલસાઇઝ સેટિંગ્સ ચેક કરો

### ફાઇલ લોક્સ ક્લીયર કરવા

જો ફાઇલ્સ લોક્ડ સ્ટેટમાં ફસાઈ જાય છે:

```bash
sudo -u www-data php /var/www/owncloud/occ maintenance:mode --on
sudo mysql -u root -p -e "DELETE FROM owncloud.oc_file_locks WHERE 1"
sudo -u www-data php /var/www/owncloud/occ maintenance:mode --off
```

## નિષ્કર્ષ

હવે તમારી પાસે તમારા રાસ્પબેરી પાઈ પર ચાલતું સંપૂર્ણ કાર્યક્ષમ, સુરક્ષિત અને ઓપ્ટિમાઇઝ્ડ પ્રાઇવેટ ક્લાઉડ સોલ્યુશન છે. ઓનક્લાઉડ તમારા ડેટા અને પ્રાઇવસી પર સંપૂર્ણ નિયંત્રણ સાથે કમર્શિયલ ક્લાઉડ સર્વિસિસનો મજબૂત અને ફીચર-રિચ વિકલ્પ પ્રદાન કરે છે.

આ સેલ્ફ-હોસ્ટેડ સોલ્યુશન કેટલાક ફાયદા ઓફર કરે છે:

- **કોઈ મંથલી ફી નહીં**: ફક્ત હાર્ડવેરનો એક-વખતનો ખર્ચ
- **અનલિમિટેડ એક્સપેન્શન**: તમારી જરૂરિયાતો વધે તેમ મોટા ડ્રાઇવ ઉમેરો
- **સંપૂર્ણ પ્રાઇવસી**: તમારો ડેટા ક્યારેય તમારા નિયંત્રણની બહાર જતો નથી
- **કસ્ટમાઇઝેશન**: ચોક્કસપણે કોન્ફિગર કરો કે તે કેવી રીતે કામ કરે
- **શીખવાની તક**: મૂલ્યવાન લિનક્સ અને સર્વર મેનેજમેન્ટ સ્કિલ્સ મેળવો

તમારા ઓનક્લાઉડ ઇન્સ્ટોલેશનને નિયમિતપણે અપડેટેડ રાખો જેથી તમને લેટેસ્ટ ફીચર્સ અને સિક્યોરિટી પેચ મળી રહે. યોગ્ય મેઇન્ટેનન્સ સાથે, તમારું સેલ્ફ-હોસ્ટેડ ક્લાઉડ સોલ્યુશન તમારા બધા ડિવાઇસ પર તમારી ફાઇલો સ્ટોર કરવા, સિંક કરવા અને શેર કરવા માટે વર્ષો સુધી વિશ્વસનીય સેવા પ્રદાન કરશે.

## વધારાના રિસોર્સિસ

- [ઓફિશિયલ ઓનક્લાઉડ ડોક્યુમેન્ટેશન](https://doc.owncloud.com/)
- [ઓનક્લાઉડ ફોરમ્સ](https://central.owncloud.org/)
- [ઓનક્લાઉડ GitHub રેપોઝિટરી](https://github.com/owncloud/core)
- [રાસ્પબેરી પાઈ ડોક્યુમેન્ટેશન](https://www.raspberrypi.org/documentation/)