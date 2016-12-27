#!/bin/sh

sleep_in_sec = 60*1

while [ true ]
do
	python event_capture_airport.py
	python event_capture_busan.py
	sleep sleep_in_sec
done

