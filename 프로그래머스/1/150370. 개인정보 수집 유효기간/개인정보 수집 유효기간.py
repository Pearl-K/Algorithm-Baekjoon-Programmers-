def solution(today, terms, privacies):
    
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d

    term_map = {k: int(v) for k, v in (t.split() for t in terms)}
    today_days = to_days(today)

    expired = []
    for idx, p in enumerate(privacies, start=1):
        date, term_type = p.split()
        collected_days = to_days(date)
        expire_days = collected_days + term_map[term_type] * 28
        if expire_days <= today_days:
            expired.append(idx)

    return expired
