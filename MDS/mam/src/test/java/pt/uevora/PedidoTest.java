package pt.uevora;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import java.time.LocalDate;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDate;


public class PedidoTest
{
    Pedido pedido;

    @Before
    public void setUp()
    {
        pedido = new Pedido("C-09", LocalDate.parse("2019-08-02"), LocalDate.parse("2019-08-08"),false);
    }

    @After
    public void down()
    {
        pedido = null;
    }

    @Test
    public void testGetDataInit() throws Exception{
        LocalDate resultado=pedido.getDataInit();
        assertEquals(LocalDate.parse("2019-08-02"),resultado);
    }

    @Test
    public void testGetDataFin() throws Exception{
        LocalDate resultado=pedido.getDataFin();
        assertEquals(LocalDate.parse("2019-08-08"),resultado);
    }

    @Test
    public void testGetDiasDisponiveis() throws Exception{
        long resultado=pedido.getDiasDisponiveis();
        assertEquals(22,resultado);
    }


}
