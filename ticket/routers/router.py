from models.model import *
from schemas.validata import *
from main import *

router = APIRouter(prefix = {"/v1/api"} , tags = [onl'Online  Ticket'])
@router.post('/path')
def creat_flight(flight: Flight)
    
