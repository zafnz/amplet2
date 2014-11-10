#ifndef _MEASURED_NSSOCK_H
#define _MEASURED_NSSOCK_H

#include <unbound.h>
#include <libwandevent.h>


/* data block given to each resolving thread */
struct amp_resolve_info {
    int fd;                     /* file descriptor to the test process */
    struct ub_ctx *ctx;         /* shared unbound context (with the cache) */
};

void resolver_socket_event_callback(wand_event_handler_t *ev_hdl, int eventfd,
        void *data, __attribute__((unused))enum wand_eventtype_t ev);

#endif