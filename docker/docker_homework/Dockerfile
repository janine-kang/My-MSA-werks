FROM edowon0623/mymysql:1.2

ENV MYSQL_ALLOW_EMPTY_PASSWORD true
ENV MYSQL_DATABASE mydb
ADD ./db_mount /var/lib/mysql

EXPOSE 3306

CMD ["mysqld"]