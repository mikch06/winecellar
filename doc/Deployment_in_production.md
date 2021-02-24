# Deployment in production

# Backup django settings.py
cp settings.py settings.py.bak

# Release
## Fetch tag's
git fetch --tag

## Check tag
git tag

## Checkout release
git checkout <tag>

## Restart app
sudo systemctl restart wine

## Recreate static files
python3 manage.py collectstatic
