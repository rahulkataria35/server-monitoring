$lines = Select-String -Path ".env" -Pattern '^\s*[^\s=]+=[^\s]+$' | Where-Object { $_.Line -notmatch '^#' }
