---
title: "Move WordPress from HTTP to HTTPS: A Complete Guide"
date: "2025-03-05"
description: "Step-by-step guide to properly migrate your WordPress site from HTTP to HTTPS using Let's Encrypt certificates"
summary: "This comprehensive tutorial walks you through the process of migrating your WordPress site from HTTP to HTTPS with Let's Encrypt SSL certificates. You'll learn how to obtain certificates, configure Apache, update WordPress settings, and ensure your site works perfectly after the migration."
tags: ["wordpress", "ssl", "https", "security", "letsencrypt", "certbot", "cloudflare", "apache"]
---

## Introduction

HTTPS is no longer optional for modern websites. Search engines favor secure sites, browsers display warning messages for non-secure sites, and visitors expect the security that HTTPS provides. This guide will walk you through the complete process of migrating your WordPress site from HTTP to HTTPS using free Let's Encrypt SSL certificates.

**Prerequisites:**

- A working WordPress site running on a LAMP server (Linux, Apache, MySQL, PHP)
- SSH access to your server
- Basic familiarity with command line
- Domain with DNS managed by Cloudflare (for wildcard certificates)

If you haven't set up WordPress on a LAMP server yet, follow our [Raspberry Pi WordPress Setup Guide](https://planetmilav.com/raspberrypisetup/) first.

## Step 1: Install Certbot

Certbot is the official Let's Encrypt client that simplifies obtaining and renewing SSL certificates. Install Certbot and the Apache plugin with the following command:

```bash
sudo apt update
sudo apt install certbot python3-certbot-apache
```

> **Note:** The original post used `python-certbot-apache -t stretch-backports` which is outdated. Modern Debian/Ubuntu distributions use the Python 3 version without needing backports.

## Step 2: Choose Your Certificate Type

You have two options for SSL certificates:

### Option A: Single Domain Certificate

If you only need to secure one domain, run:

```bash
sudo certbot --apache
```

This will guide you through an interactive process to select which domains to secure and automatically configure Apache for you.

For more control, you can use:

```bash
sudo certbot certonly --apache
```

This obtains the certificate without modifying your Apache configuration, giving you more control over the setup.

### Option B: Wildcard Certificate with Cloudflare DNS (Recommended)

A wildcard certificate covers your main domain and all subdomains (e.g., `example.com` and `*.example.com`). This is ideal if you run multiple subdomains.

1. Install the Cloudflare DNS plugin for Certbot:

```bash
sudo pip3 install certbot-dns-cloudflare
```

2. Create a Cloudflare API configuration file:

```bash
sudo mkdir -p /etc/letsencrypt/
sudo nano /etc/letsencrypt/cloudflare.ini
```

3. Add your Cloudflare account details:

```ini
dns_cloudflare_email = 'your-cloudflare-email@example.com'
dns_cloudflare_api_key = 'your-global-api-key'
```

> **Security Note:** To obtain your Global API key, log in to Cloudflare, go to your profile, and look for the API Tokens section. For better security, consider using scoped API tokens instead of the global key.

4. Secure the configuration file to prevent unauthorized access:

```bash
sudo chmod 600 /etc/letsencrypt/cloudflare.ini
```

5. Obtain the wildcard certificate:

```bash
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials /etc/letsencrypt/cloudflare.ini -d yourdomain.com,*.yourdomain.com --preferred-challenges dns-01
```

Replace `yourdomain.com` with your actual domain name.

## Step 3: Configure Apache for HTTPS

### Configure Default SSL Site

If your WordPress site is in the default `/var/www/html` directory, edit the default SSL configuration:

```bash
sudo nano /etc/apache2/sites-available/default-ssl.conf
```

Update the file with the following content (replace `yourdomain.com` with your domain):

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

If your site is in a custom directory, adjust the `DocumentRoot` and `<Directory>` paths accordingly.

### Enable SSL Modules and the Configuration

```bash
sudo a2enmod ssl
sudo a2enmod headers
sudo a2ensite default-ssl.conf
sudo systemctl restart apache2
```

### Configure HTTP to HTTPS Redirection (Recommended)

Edit your HTTP VirtualHost configuration:

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

Add the following redirection rules inside the `<VirtualHost *:80>` block:

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    
    # Other configuration...
    
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>
```

Enable the rewrite module and restart Apache:

```bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

## Step 4: Update WordPress Settings

### Update Site URLs in WordPress Admin

1. Log in to your WordPress admin dashboard
2. Go to Settings → General
3. Update both "WordPress Address (URL)" and "Site Address (URL)" to use `https://` instead of `http://`
4. Save changes

If you encounter issues (like a white screen or login problems) after changing these settings, you can fix them using MySQL:

```bash
mysql -u root -p
use wordpress;   # Replace with your actual database name if different
update wp_options set option_value = 'https://yourdomain.com' where option_name = 'siteurl';
update wp_options set option_value = 'https://yourdomain.com' where option_name = 'home';
exit;
```

### Modify wp-config.php

Add the following code to your `wp-config.php` file, right before the line that says `require_once(ABSPATH . 'wp-settings.php');`:

```php
/* SSL Settings */
define('FORCE_SSL_ADMIN', true);

/* Turn HTTPS 'on' for proper WordPress detection */
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
    $_SERVER['HTTPS'] = 'on';
}
```

This ensures WordPress properly detects HTTPS, especially when behind proxies or load balancers.

## Step 5: Update Internal Links in Your Database

The database may contain hardcoded HTTP links in posts, pages, and options. Use the "Better Search Replace" plugin to fix these:

1. Install the "Better Search Replace" plugin (it's safer and more feature-rich than the older "Search and Replace" plugin)
2. Go to Tools → Better Search Replace
3. In the "Search for" field, enter `http://yourdomain.com`
4. In the "Replace with" field, enter `https://yourdomain.com`
5. Select all tables except those containing transients
6. Enable the "Run as dry run" option first to see what would be changed
7. If the results look good, uncheck "Run as dry run" and run the search/replace for real

## Step 6: Set Up Automatic Certificate Renewal

Let's Encrypt certificates expire after 90 days, so setting up automatic renewal is crucial:

```bash
sudo crontab -e
```

Add the following line to run the renewal check twice daily (recommended by Let's Encrypt):

```bash
0 3,15 * * * certbot renew --quiet --post-hook "systemctl reload apache2" > /dev/null 2>&1
```

## Step 7: Test Your HTTPS Setup

Visit these tools to verify your SSL configuration:

1. [SSL Labs Server Test](https://www.ssllabs.com/ssltest/)
2. [Why No Padlock](https://www.whynopadlock.com/)

Check for:

- Valid certificate
- No mixed content warnings
- Proper redirects

## Troubleshooting

### Mixed Content Warnings

If you see mixed content warnings in your browser console:

1. Use the "Better Search Replace" plugin again to find any remaining `http://` references
2. Check your theme and plugin files for hardcoded HTTP URLs
3. Consider using the "Really Simple SSL" plugin to automatically fix mixed content issues

### White Screen After URL Change

If you encounter a white screen:

1. Try accessing wp-admin directly with HTTPS
2. Use the MySQL fix mentioned earlier
3. Verify file permissions and ownership

### Certificate Renewal Issues

If automatic renewal fails:

1. Test the renewal process manually: `sudo certbot renew --dry-run`
2. Check logs: `sudo journalctl -xe`
3. Ensure the Cloudflare API credentials are correct (for wildcard certificates)

## Conclusion

Congratulations! Your WordPress site is now fully secured with HTTPS. This improves your site's security, SEO ranking, and user trust. Remember to:

- Monitor certificate expiration (though automatic renewal should handle this)
- Keep an eye on mixed content warnings when adding new content
- Consider additional security measures like HTTP Strict Transport Security (HSTS)

With SSL properly configured, your WordPress site is now more secure and ready for the modern web!

## Additional Resources

- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)
- [Certbot Instructions](https://certbot.eff.org/)
- [WordPress HTTPS Migration Guide](https://www.wpbeginner.com/wp-tutorials/how-to-add-ssl-and-https-in-wordpress/)
- [Cloudflare SSL Documentation](https://developers.cloudflare.com/ssl/)
