package com.sistemasdistribuidos.mqtt;

import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;
import java.io.InputStream;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;

public class TLSUtil {

    public static SSLContext createSSLContext(String resourceName) throws Exception {

        // Carregar o arquivo a partir do classpath (resources)
        InputStream is = TLSUtil.class.getClassLoader().getResourceAsStream(resourceName);

        if (is == null) {
            throw new RuntimeException("Certificado não encontrado no classpath: " + resourceName);
        }

        CertificateFactory cf = CertificateFactory.getInstance("X.509");
        X509Certificate caCert = (X509Certificate) cf.generateCertificate(is);

        KeyStore ks = KeyStore.getInstance(KeyStore.getDefaultType());
        ks.load(null);
        ks.setCertificateEntry("caCert", caCert);

        TrustManagerFactory tmf =
                TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        tmf.init(ks);

        SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(null, tmf.getTrustManagers(), new SecureRandom());

        return sslContext;
    }
}
