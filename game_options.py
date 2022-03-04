from collections import namedtuple

options_tuple = namedtuple("options_tuple", [
                            "left_slider",
                            "pulsar"
                        ]  
                )

def options_map(width: int, height:int , scale: int):
    rows = int(height / scale)
    columns = int(width / scale)
    
    row_mid = int(rows/2)
    col_mid = int(columns/2)
    return options_tuple(
        set([(row_mid,col_mid), (row_mid +1,col_mid), (row_mid + 2, col_mid),  (row_mid, col_mid + 1), (row_mid + 1, col_mid + 2)]), 
        set([
                (row_mid,col_mid), (row_mid + 1, col_mid), (row_mid + 3, col_mid),   (row_mid + 3,col_mid), (row_mid + 4, col_mid), (row_mid + 5, col_mid),   
                (row_mid + 4, col_mid + 2), (row_mid + 4, col_mid + 3), (row_mid + 4, col_mid + 4),  (row_mid - 2, col_mid + 2), (row_mid - 2, col_mid + 3), (row_mid - 2, col_mid + 4),   (row_mid + 2, col_mid + 2),(row_mid + 2, col_mid + 3),(row_mid + 2,col_mid + 4),  (row_mid + 7, col_mid + 2),(row_mid + 7, col_mid + 3),(row_mid + 7,col_mid + 4),
                (row_mid,col_mid + 5), (row_mid + 1, col_mid + 5), (row_mid + 3, col_mid + 5),   (row_mid + 3,col_mid + 5), (row_mid + 4, col_mid + 5), (row_mid + 5, col_mid + 5),

                (row_mid,col_mid + 7), (row_mid + 1, col_mid + 7), (row_mid + 3, col_mid + 7),   (row_mid + 3,col_mid + 7), (row_mid + 4, col_mid + 7), (row_mid + 5, col_mid + 7),   
                (row_mid + 4, col_mid + 8), (row_mid + 4, col_mid + 9), (row_mid + 4, col_mid + 10),  (row_mid - 2, col_mid + 8), (row_mid - 2, col_mid + 9), (row_mid - 2, col_mid + 10),   (row_mid + 2, col_mid + 8),(row_mid + 2, col_mid + 9),(row_mid + 2,col_mid + 10),  (row_mid + 7, col_mid + 8),(row_mid + 7, col_mid + 9),(row_mid + 7,col_mid + 10),
                (row_mid,col_mid + 12), (row_mid + 1, col_mid + 12), (row_mid + 3, col_mid + 12),   (row_mid + 3,col_mid + 12), (row_mid + 4, col_mid + 12), (row_mid + 5, col_mid + 12)
            ] 
        )
    )
