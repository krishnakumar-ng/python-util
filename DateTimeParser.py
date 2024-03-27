import sys
from datetime import datetime

class DateTimeParser:

    @staticmethod
    def parse_input(input_time):
        try:
            # Try to parse input time as an integer (epoch time)
            if input_time.lower() == "now":
                return datetime.now()
            
            elif input_time.isdigit():
                # If input is a digit, assume it's epoch time in seconds
                return datetime.fromtimestamp(int(input_time))
            
            elif input_time.isdigit() and len(input_time) == 13:
                # If input is a 13-digit number, assume it's epoch time in milliseconds
                return datetime.fromtimestamp(int(input_time) / 1000)
            
            elif input_time.isdigit() and len(input_time) == 19:
                # If input is a 19-digit number, assume it's epoch time in nanoseconds
                return datetime.fromtimestamp(int(input_time) / 1e9)

            else:
                # Try to parse input time using various formats
                formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%d %H:%M:%S.%f%z', '%Y-%m-%d %H:%M:%S.%f']
                for format in formats:
                    try:
                        parsed_time = datetime.strptime(input_time, format)
                        return parsed_time
                    except ValueError:
                        continue
                
                # If unable to parse, raise an error
                raise ValueError("Invalid input format!")
            
        except Exception as e:
            print("Error:", e)
            sys.exit(1)