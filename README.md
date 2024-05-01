# AskMe
## NGINX
|          | min | mean  | +/-sd | median | max  |
|----------|-----|-------|-------|--------|------|
| Connect  | 0   | 4     | 63.5  | 0      | 1008 |
| Processing | 5  | 13    | 8.5   | 12     | 209  |
| Waiting   | 1   | 10    | 6.9   | 10     | 209  |
| Total     | 5   | 17    | 67.1  | 12     | 1218 |

## qunicorn static
|          | min | mean | +/-sd | median | max |
|----------|-----|------|-------|--------|-----|
| Connect  | 0   | 5    | 1.0   | 5      | 8   |
| Processing | 3  | 8    | 2.5   | 8      | 20  |
| Waiting  | 0   | 6    | 2.0   | 6      | 15  |
| Total    | 8   | 13   | 2.1   | 13     | 25  |


## gunicorn dinamic
|          | min | mean | +/-sd | median | max |
|----------|-----|------|-------|--------|-----|
| Connect  | 0   | 1    | 2.1   | 0      | 7   |
| Processing | 3  | 44   | 8.1   | 44     | 69  |
| Waiting   | 3   | 43   | 8.1   | 44     | 69  |
| Total     | 9   | 45   | 7.4   | 44     | 73  |


## NGINX->gunicorn
|          | min | mean | +/-sd | median | max |
|----------|-----|------|-------|--------|-----|
| Connect  | 0   | 1    | 1.5   | 0      | 5   |
| Processing | 6  | 45   | 11.0  | 50     | 65  |
| Waiting   | 1   | 45   | 11.3  | 50     | 65  |
| Total     | 6   | 46   | 9.7   | 50     | 65  |


## NGINX->gunicorn+cache
|          | min | mean | +/-sd | median | max |
|----------|-----|------|-------|--------|-----|
| Connect  | 0   | 4    | 1.0   | 4      | 6   |
| Processing | 1  | 6    | 1.9   | 6      | 12  |
| Waiting   | 0   | 4    | 1.6   | 4      | 9   |
| Total     | 4   | 10   | 1.8   | 10     | 13  |


