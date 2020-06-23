ln -s ~/var/www/myblog/config/myblog.conf /etc/supervisord.d/myblog.conf
supervisorctl update
#supervisorctl
ln -s ~/var/www/myblog/config/myblog.nginx /etc/nginx/sites-available/myblog.nginx
ln -s /etc/nginx/sites-available/myblog.nginx /etc/nginx/sites-enabled/myblog.nginx
