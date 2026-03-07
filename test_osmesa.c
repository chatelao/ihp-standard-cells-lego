#include <GL/osmesa.h>
#include <stdio.h>

int main() {
    OSMesaContext ctx = OSMesaCreateContext(OSMESA_RGBA, NULL);
    if (!ctx) {
        printf("OSMesaCreateContext failed!\n");
        return 1;
    }
    printf("OSMesaCreateContext succeeded!\n");
    OSMesaDestroyContext(ctx);
    return 0;
}
