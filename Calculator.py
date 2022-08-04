from ShipMap import api_offset_map


class CoordinatesCalculator:

    @staticmethod
    def calculate(coordinates):
        zoom = CoordinatesCalculator.__get_zoom(coordinates)
        rectangles = CoordinatesCalculator.__calculate_rectangles(coordinates, zoom)
        center = CoordinatesCalculator.__get_center(coordinates)
        response = CoordinatesCalculator.__prepare_response(center, rectangles, zoom)
        return response

    @staticmethod
    def __get_zoom(coordinates):
        rectangle_size = CoordinatesCalculator.__calculate_rectangle_size(coordinates)
        zoom = CoordinatesCalculator.__calculate_zoom(rectangle_size)
        return zoom

    @staticmethod
    def __calculate_rectangle_size(coordinates):
        x_top = CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['x'])
        x_bot = CoordinatesCalculator.transform_coordinate_to_float(coordinates[1]['x'])
        y_top = CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['y'])
        y_bot = CoordinatesCalculator.transform_coordinate_to_float(coordinates[1]['y'])
        x_size = (x_top - x_bot)/4
        y_size = (y_top - y_bot)/3
        return {"x": abs(round(x_size, 3)), "y": round(y_size, 3)}

    @staticmethod
    def __calculate_zoom(rect_size):
        zoom = 2
        for i in range(2, 19):
            rect_num = 2**(i-1)
            rect_x = round(360/rect_num, 3)
            rect_y = round(180/rect_num, 3)
            if rect_size['x'] > rect_x or rect_size['y'] > rect_y:
                zoom = i-2
                break
        return zoom

    @staticmethod
    def __calculate_rectangles(coordinates, zoom):
        x_top = CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['x'])
        y_top = -CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['y'])
        rect_num = 2**(zoom-1)
        rect_x = 360/rect_num
        rect_y = 320/rect_num
        x_found = y_found = False
        num = 0
        start_x = start_y = 0
        for i in range(-rect_num//2, rect_num//2, 1):
            num += 1
            current_x = rect_x*i
            current_y = rect_y*i
            if not x_found and current_x > x_top:
                start_x = num-1
                x_found = True
            if not y_found and current_y > y_top:
                if str(zoom) not in api_offset_map:
                    start_y = num
                else:
                    start_y = num + api_offset_map[str(zoom)]
                y_found = True
            if x_found and y_found:
                break
        rectangles = []
        for i in range(4):
            for j in range(2):
                rect = {
                    "x": start_x + i,
                    "y": start_y + j,
                    "z": zoom
                }
                rectangles.append(rect)
        return rectangles

    @staticmethod
    def transform_coordinate_to_float(coordinate):
        coord = abs(coordinate['degree']) + (coordinate['minute'] + coordinate['second'] / 60) / 60
        # if coordinate['degree'] < 0:
        #     coord = -coord
        if 'hemisphere' in coordinate:
            if coordinate['hemisphere'] == 's' or coordinate['hemisphere'] == 'w':
                coord = -coord
        return coord

    @staticmethod
    def transform_float_to_coordinate(float_coord):
        coord = {
            "degree": int(float_coord),
            "minute": int(float_coord % 1 * 60),
            "second": round(float_coord % 1 * 60 % 1 * 60, 2)
        }
        return coord

    @staticmethod
    def __get_center(coordinates):
        x_top = CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['x'])
        x_bot = CoordinatesCalculator.transform_coordinate_to_float(coordinates[1]['x'])
        y_top = CoordinatesCalculator.transform_coordinate_to_float(coordinates[0]['y'])
        y_bot = CoordinatesCalculator.transform_coordinate_to_float(coordinates[1]['y'])
        x_mid = round(abs((x_top - x_bot)/2) + x_top, 3)
        y_mid = round(abs((y_top - y_bot)/2) + y_bot, 3)
        return {
            "x": x_mid,
            "y": y_mid
        }

    @staticmethod
    def __prepare_response(center, rectangles, zoom):
        response = {
            "page": {
                "x": center['x'],
                'y': center['y'],
                'z': zoom
            },
            "blocks": rectangles
        }
        return response