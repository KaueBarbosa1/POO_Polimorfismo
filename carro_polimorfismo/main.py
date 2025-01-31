from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main__":
    carro_inteligente = CarroInteligente(10)
    carro_inteligente.estacionar()
    test_drive(carro_inteligente)

    carro_esportivo = CarroEsportivo(50)
    carro_esportivo.turbo()
    test_drive(carro_esportivo)

    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)