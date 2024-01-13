# from flask import Flask
# import os
#
#
# app = Flask(__name__)
#
# #
# # @app.route('/')
# # def index():
# #     return render_template('tamplates/sample_index.html')
#
#
# @app.route('/')
# def api():
#     with open(
#         os.path.join(os.getcwd(), 'data', 'data.json'), mode='r'
#     ) as my_file:
#         text = my_file.read()
#         return text
#
#
#
# # @app.route('/success', methods=['POST', 'GET'])
# # def success():
# #     if request.method == 'POST':
# #         main_field = request.form['main_field']
# #         print(main_field)
# #         data = product_details_by_name(main_field)
# #         addRow(data)
# #
# #     return render_template('tamplates/success.html')
#
# # Debug only
# app.run(host='0.0.0.0', port=94, debug=True)
