package pt.uevora;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDate;

public class UserTest
{

    User user;

    @Before
    public void setUp(){

        user=new User("C-09","adf");

    }

    @After
    public void down(){
        user=null;
    }

   @Test
    public void testGetUsername() throws Exception{
        String resultado=user.getUsername();
        assertEquals("C-09",resultado);
   }

   @Test
    public void testGetPassword() throws Exception{
        String resultado=user.getPassword();
        assertEquals("adf",resultado);
   }

   @Test
    public void testGetDiasDisponiveis() throws Exception{
        long resultado=user.getDiasDisponiveis();
        assertEquals(22,resultado);
   }

   @Test
    public void testCalcularPontos() throws Exception{
        long resultado=user.calculaPontos(5,3);
        assertEquals(6,resultado);
   }

   @Test
   public void testPontos() throws Exception{
      long resultado=user.pontos(3, LocalDate.parse("2019-2-8"),LocalDate.parse("2019-2-12"));
      assertEquals(12,resultado);

   }

}
