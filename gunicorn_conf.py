from multiprocessing import cpu_count


# Socket Path
bind = 'unix:/home/arnoliono/admerkcorp/backend/gunicorn.sock'


# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'


# Logging Options
loglevel = 'debug'
accesslog = '/home/arnoliono/admerkcorp/backend/access_log'
errorlog =  '/home/arnoliono/admerkcorp/backend/error_log'