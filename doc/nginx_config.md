### server
- redirect everything to https


    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        root         /var/www;
        return 301 https://$host$request_uri;

        include /etc/nginx/default.d/*.conf;
        return 444;


### vhost

    server {
        listen  443 ssl;
        server_name <fqdn> <fqdn-alias>;

            location /static/ {
                    alias /opt/django-winecellar/wine/static/;
            }

            location / {
                    proxy_pass http://127.0.0.1:8000;
            }

        location = /favicon.ico {
                alias /opt/wine/django-winecellar/static/favicon.ico;
        }

