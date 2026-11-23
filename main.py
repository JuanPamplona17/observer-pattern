from abc import ABC, abstractmethod


# Interfaz Sujeto
class Sujeto(ABC):

    @abstractmethod
    def registrar(self, observador):
        pass

    @abstractmethod
    def eliminar(self, observador):
        pass

    @abstractmethod
    def notificar(self, reportero, noticia):
        pass


# Interfaz Observador
class Observador(ABC):

    @abstractmethod
    def actualizar(self, reportero, noticia):
        pass


# Clase principal del sistema de noticias
class Noticias(Sujeto):

    def __init__(self):
        self.observadores = []

    def registrar(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar(self, reportero, noticia):
        for observador in self.observadores:
            observador.actualizar(reportero, noticia)

    def publicar(self, reportero, noticia):
        print(f"\nEsperando noticia: {reportero} - {noticia}")
        self.notificar(reportero, noticia)


# Observador: Página Web
class Web(Observador):

    def actualizar(self, reportero, noticia):
        print(f"Web - {noticia}")


# Observador: Canal de televisión
class TVChannel(Observador):

    def actualizar(self, reportero, noticia):
        print(f"TV - {noticia}")


# Observador: Aplicación móvil
class AppMovil(Observador):

    def actualizar(self, reportero, noticia):
        print(f"App - {noticia}")


# Clase Reportero
class Reportero:

    def __init__(self, nombre, sistema):
        self.nombre = nombre
        self.sistema = sistema

    def publicar_noticia(self, noticia):
        self.sistema.publicar(self.nombre, noticia)


# Programa principal
if __name__ == "__main__":

    # Crear el sistema de noticias
    sistema = Noticias()

    # Registrar los tres medios de comunicación
    sistema.registrar(Web())
    sistema.registrar(TVChannel())
    sistema.registrar(AppMovil())

    # Crear los cuatro reporteros
    reportero1 = Reportero("Reportero 1", sistema)
    reportero2 = Reportero("Reportero 2", sistema)
    reportero3 = Reportero("Reportero 3", sistema)
    reportero4 = Reportero("Reportero 4", sistema)

    # Simular la publicación de noticias
    reportero1.publicar_noticia("La bolsa ha caído")

    reportero2.publicar_noticia(
        "Se anuncian nuevas medidas económicas"
    )

    reportero3.publicar_noticia(
        "El Real Madrid de nuevo gana la Champions"
    )

    reportero4.publicar_noticia(
        "Se presentan nuevos avances tecnológicos"
    )
