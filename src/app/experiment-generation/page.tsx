"use client";

import React, { useEffect, useRef, useState } from "react";
import {
  Box,
  Center,
  Heading,
  VStack,
  Button,
  Image,
  Text,
  Flex,
  Link,
  Spacer,
  FormControl,
  FormLabel,
  Textarea,
  SlideFade,
  IconButton,
  Skeleton,
} from "@chakra-ui/react";
import { DownloadIcon } from "@chakra-ui/icons";
import Navbar from "@/components/navbar";

export default function ExperimentGenerationPage() {
  const [text, setText] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = () => {
    setSubmitted(true);
  };

  const [imageGenerated, setImageGenerated] = useState(false);
  const [generatedImageUrl, setGeneratedImageUrl] = useState("");

  const [isLoading, setIsLoading] = useState(false);

  let handleInputChange = (e: { target: { value: any; }; }) => {
    let inputValue = e.target.value
    setText(inputValue)
  }

  const handleGenerateClick = () => {
    setImageGenerated(false);
    setIsLoading(true);
    setTimeout(() => {
      const url = "procedure.png";
      setGeneratedImageUrl(url);
      setImageGenerated(true);
      setIsLoading(false);
    }, 5000);
  };

  const videoBlurStyle = `
  .background-video {
    -webkit-filter: blur(8px); /* Chrome, Safari, Opera */
    filter: blur(8px); /* Standard syntax */
  }
`;
  const videoRef = useRef<HTMLVideoElement>(null);

//   useEffect(() => {
//     if (videoRef.current) {
//       videoRef.current.playbackRate = 0.7;
//     }
//   }, []);

  return (
    <Box>
      <Navbar />

      <Box height="100vh" px={"3vw"} color="black">
        <>
          <style>{videoBlurStyle}</style>
          <Box
            as="video"
            autoPlay
            loop
            muted
            playsInline
            position="absolute"
            zIndex="-1"
            top="0"
            left="0"
            backdropBlur={8}
            // filter="auto"
            // blur="4px"
            ref={videoRef}
          >
            <source src="/background3.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </Box>
        </>
        <Box
          position="fixed"
          top="0"
          left="0"
          width="100vw"
          height="100vh"
          zIndex="-1"
          bgGradient="linear(to-tr, brand.300, brand.500)"
          opacity="0.5"
        ></Box>
        <Flex h={"full"} alignItems={"center"} justifyContent={"center"} px="5">
          <VStack
            boxShadow="dark-lg"
            borderRadius={"20px"}
            p="10"
            alignItems={"left"}
            justifyContent={"center"}
            spacing={5}
            width={"35vw"}
            backdropFilter={"blur(8px) brightness(150%)"}
          >
            <Text
              lineHeight="55px"
              fontSize="5xl"
              fontWeight="semi-bold"
              align={"left"}
              color="white"
            >
              Experiment Generation
            </Text>
            <Text fontSize="large" align={"left"} color="white">
            Enter your experimental protocol or description of procedure here! SciSketch will automatically extract key reagents, experimental materials, animal/cell models used, as well as key experimental steps to illustrate the experiment graphically.
            </Text>
          </VStack>

          <Spacer />

          <VStack
            boxShadow="dark-lg"
            spacing={4}
            // align="stretch"
            mt={4}
            width="50vw"
            backdropFilter={"blur(8px) brightness(150%)"}
            borderRadius={"20px"}
            px="5"
            pt="5"
          >
            <Textarea
              placeholder="Enter your text here..."
              size="md"
              background={"white"}
              height={"20vh"}
              value={text}
              onChange={handleInputChange}
            />
            <Button
              color="white"
              boxShadow="dark-lg"
              bg="brand.400"
              _hover={{
                color: "gray",
                bgGradient: "linear(to-tr, brand.200, brand.500)",
              }}
              onClick={handleGenerateClick}
              size="lg"
              isLoading={isLoading}
              loadingText="Generating..."
              disabled={isLoading}
            >
              Generate
            </Button>
            <Box position="relative">
              {imageGenerated && (
                // <Skeleton
                //   my="4"
                //   startColor="brand.500"
                //   endColor="brand.100"
                //   height="40vh"
                //   borderRadius={"10"}
                // ></Skeleton>
                <Image
                  src={generatedImageUrl}
                  alt="Generated Image"
                  borderRadius={"10"}
                  boxShadow="dark-lg"
                  width="200px"
                  scale={0.5}
                  // height="40vh"
                  my="4" />
              )}
            </Box>
          </VStack>
        </Flex>
      </Box>
    </Box>
  );
}
