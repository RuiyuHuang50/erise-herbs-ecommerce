# Render Deployment Configuration

## Required Settings in Render Dashboard:

### Build Command:
```
./build.sh
```

### Start Command:
```
gunicorn ecommerce.wsgi:application
```

### Environment Variables:
```
DEBUG=False
PYTHON_VERSION=3.11.6
```

### Root Directory:
```
(leave empty)
```

### Branch:
```
main
```

## Important Notes:
- Make sure to use Python 3.11.6 (specified in runtime.txt)
- The start command MUST be: gunicorn ecommerce.wsgi:application
- NOT: gunicorn app:app (this is the common mistake)

## If deployment fails:
1. Check that build command is: ./build.sh
2. Check that start command is: gunicorn ecommerce.wsgi:application
3. Make sure Python version is 3.11.6
4. Environment variable DEBUG should be False