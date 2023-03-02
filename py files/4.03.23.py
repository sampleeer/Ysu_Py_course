s1 = 'abc'
s2 = 'def'
print(s1 + s2)
num = 10
head = 'John Doe'
print(f'our boss {head} has {num} subordinates') #конкатенация строк и к одному типу
print(','.join(['1', '2']))

candidate = input()
try:
    print(float(candidate))
except Exception as e:
    print('Not float')

from typing import Any, Dict, List, Optional, Tuple, Union
def process_employees_dict(employees_dict: dict) -> int:
    return None

DutyList = Union[List[float], List[str]]

def process_employees_dict(
        employees_dict: Dict[str, Any],
        duty_list: DutyList,
        days_boss_angry: Optional[List[str]] = None
) -> Optional[Tuple[int, str]]:
    if days_boss_angry is not None:
        return 1, 'jenga'
    return None