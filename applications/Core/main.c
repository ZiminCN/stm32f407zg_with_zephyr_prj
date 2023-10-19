#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(main, LOG_LEVEL_INF);

int main(){

    LOG_INF("f407_prj start!");
    printk("printk test");

    return 0;
}