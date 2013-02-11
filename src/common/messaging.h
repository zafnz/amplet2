#ifndef _MEASURED_MESSAGING_H
#define _MEASURED_MESSAGING_H

#include <amqp.h>
#include <amqp_framing.h>
#include "tests.h"


/* local broker will persist it for us and send to master server later */
#define AMQP_SERVER "localhost"

/* 5672 is default, 5671 for SSL */
#define AMQP_PORT 5672

/* 128KB, recommended default */
#define AMQP_FRAME_MAX 131072


amqp_connection_state_t conn;


int connect_to_broker(void);
void close_broker_connection(void);
int report_to_broker(test_type_t type, uint64_t timestamp, void *bytes, 
	size_t len);

#endif