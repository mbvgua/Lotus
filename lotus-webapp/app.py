from website import create_app

app = create_app()

if __name__ == '__main__':
	# app.run(debug=True, host='192.168.0.1', port=80) 
	app.run(debug=True) 