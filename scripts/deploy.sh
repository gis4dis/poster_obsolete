ERRORSTRING="Usage: ./deploy web [go|manage]"

if [ $# -eq 0 ]
    then
        echo $ERRORSTRING;
elif [ $1 == "web" ]
    then
        if [[ -z $2 ]]
            then
                cd darksheep;git pull; cd -;
                echo "Running dry-run"
                rsync --dry-run -az --force --delete --progress --exclude-from=deploy_exclude.txt ../src/ /opt/poster-app/src
        elif [ $2 == "go" ]
            then
                echo "Running actual deploy"
                rsync -az --force --delete --progress --exclude-from=deploy_exclude.txt ../src/ /opt/poster-app/src
        elif [ $2 == "manage" ]
            then
                echo "Running manage scripts"
                source /opt/poster-app/virtualenv/bin/activate
                cd /opt/poster-app/src; python manage.py collectstatic -c; python manage.py migrate --noinput
                chown poster-app:poster-app /opt/poster-app/src -R
        else
            echo $ERRORSTRING;
        fi
fi
