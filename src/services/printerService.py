import win32print

class PrinterService:
    def get_printer_list():
        printer_default = win32print.GetDefaultPrinter()
        printers = [printer_default]

        for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS):
            if printer[2] not in printers:
                printers.append(printer[2])

        return printers

    def get_printer_jobs(printer_name=None):
        if printer_name is None:
            printer_name = win32print.GetDefaultPrinter()

        jobs = []
        
        hPrinter = win32print.OpenPrinter(printer_name)
        job_info = win32print.EnumJobs(hPrinter, 0, -1, 1)
        for job in job_info:
            jobs.append({
                'job_id': job['JobId'],
                'document': job['pDocument'],
                'status': job['Status'],
                'pages': job['TotalPages'],
            })
        win32print.ClosePrinter(hPrinter)
        

        return jobs